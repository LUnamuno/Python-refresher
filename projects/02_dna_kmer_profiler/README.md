# Project 02 - DNA k-mer profiler

Count k-mers (all substrings of length k) of DNA sequences with three different implementations and compare how they scale.

**Skills:** strings, `dict`/`collections.Counter`, generators, NumPy vectorisation, timing and profiling, empirical complexity.
**Notebooks to review first:** 01 (basics), 04 (iterators and generators), 06 (NumPy), 11 (profiling).

## How to work

1. Open `kmer_profiler.py`; `random_dna` is provided, the rest is yours (docstrings = specification).
2. `python -m pytest projects/02_dna_kmer_profiler -q` (skipped = not implemented yet).
3. Tests marked `slow` check performance; run only the fast ones with `-m "not slow"`.

## Milestones

1. Basic sequence tools - `gc_content`, `reverse_complement`.
2. Three counters - `count_kmers_naive` (plain dict), `count_kmers_counter` (`Counter` + generator), `count_kmers_numpy` (integer encoding + `numpy.bincount`/`unique`). All must return the same result.
3. `frequencies` - relative frequencies.
4. Benchmarks - `best_time`, `extrapolate_hours`, `compare_implementations`.

## Stretch goals

- Profile the naive version with `cProfile` and `line_profiler`; write down what you find.
- Read sequences from a FASTA file with a generator that never loads the whole file in memory.
- Add canonical k-mers (a k-mer and its reverse complement counted together).
- Plot running time vs sequence length for the three versions with matplotlib (notebook 07).
