import pytest

from kmer_profiler import (
    best_time,
    compare_implementations,
    count_kmers_counter,
    count_kmers_naive,
    count_kmers_numpy,
    extrapolate_hours,
    frequencies,
    gc_content,
    random_dna,
    reverse_complement,
)

IMPLEMENTATIONS = [count_kmers_naive, count_kmers_counter, count_kmers_numpy]


def test_random_dna_is_reproducible():                  # PROVIDED helper: this test must pass from the start
    assert random_dna(50, seed=1) == random_dna(50, seed=1)
    assert random_dna(50, seed=1) != random_dna(50, seed=2)
    assert set(random_dna(1000)) == set("ACGT")


@pytest.mark.parametrize("impl", IMPLEMENTATIONS)
def test_known_counts(impl):
    assert impl("ACGACG", 2) == {"AC": 2, "CG": 2, "GA": 1}
    assert impl("AAAA", 1) == {"A": 4}
    assert impl("AAAA", 3) == {"AAA": 2}
    assert impl("ACGT", 4) == {"ACGT": 1}


@pytest.mark.parametrize("impl", IMPLEMENTATIONS)
def test_edge_cases(impl):
    assert impl("", 2) == {}
    assert impl("AC", 5) == {}
    with pytest.raises(ValueError):
        impl("ACGT", 0)
    with pytest.raises(ValueError):
        impl("ACGT", -1)


@pytest.mark.parametrize("k", [1, 2, 3, 4, 6])
def test_implementations_agree(k):
    seq = random_dna(5_000, seed=k)
    expected = count_kmers_naive(seq, k)
    assert sum(expected.values()) == len(seq) - k + 1
    assert count_kmers_counter(seq, k) == expected
    assert count_kmers_numpy(seq, k) == expected


def test_return_types():
    for impl in IMPLEMENTATIONS:
        result = impl("ACGTACGT", 2)
        assert type(result) is dict
        assert all(isinstance(v, int) for v in result.values())


def test_gc_content():
    assert gc_content("") == 0.0
    assert gc_content("GGCC") == 1.0
    assert gc_content("ATAT") == 0.0
    assert gc_content("ACGT") == pytest.approx(0.5)
    assert 0.45 < gc_content(random_dna(20_000)) < 0.55


def test_reverse_complement():
    assert reverse_complement("AACG") == "CGTT"
    assert reverse_complement("") == ""
    seq = random_dna(100)
    assert reverse_complement(reverse_complement(seq)) == seq


def test_frequencies():
    assert frequencies({}) == {}
    freq = frequencies({"A": 1, "C": 3})
    assert freq == {"A": 0.25, "C": 0.75}
    assert sum(frequencies(count_kmers_naive(random_dna(1000), 2)).values()) == pytest.approx(1.0)


def test_best_time_and_extrapolation():
    assert 0 < best_time(sum, range(10_000)) < 1
    assert extrapolate_hours(1.0, 1_000_000, 3_600_000_000) == pytest.approx(1.0)
    assert extrapolate_hours(10, 1_000, 2_000) == pytest.approx(20 / 3600)


@pytest.mark.slow
def test_numpy_version_is_faster():
    timings = compare_implementations(n=400_000, k=3)
    assert set(timings) == {"naive", "counter", "numpy"}
    assert timings["numpy"] < timings["naive"], timings
