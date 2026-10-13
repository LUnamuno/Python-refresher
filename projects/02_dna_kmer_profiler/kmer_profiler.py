"""Project 02 - DNA k-mer profiler: count nucleotides / dinucleotides / trinucleotides, then make it fast.

(Bonus-slides exercise: *how long would it take to analyse the human genome, 3.5 billion bases?*)

Fill in every function marked ``raise NotImplementedError`` and run::

    python -m pytest projects/02_dna_kmer_profiler -q
"""
from __future__ import annotations
import random
import time
from collections import Counter
from collections.abc import Callable
import numpy as np
ALPHABET = 'ACGT'
COMPLEMENT = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A'}
HUMAN_GENOME_BASES = 3500000000

def random_dna(n: int, seed: int=0) -> str:
    """PROVIDED. A reproducible random DNA string of length ``n`` over A, C, G, T."""
    rng = random.Random(seed)
    return ''.join(rng.choices(ALPHABET, k=n))

def count_kmers_naive(seq: str, k: int) -> dict[str, int]:
    """Count every overlapping substring of length ``k`` with an explicit ``for`` loop and a plain ``dict``
    (no ``Counter``). ``k <= 0`` -> ``ValueError``; ``k > len(seq)`` -> ``{}``.

    ``count_kmers_naive("ACGACG", 2) == {"AC": 2, "CG": 2, "GA": 1}``
    """
    raise NotImplementedError

def count_kmers_counter(seq: str, k: int) -> dict[str, int]:
    """Same result as ``count_kmers_naive`` but idiomatic: ``collections.Counter`` over a generator expression.
    Return a plain ``dict``."""
    raise NotImplementedError

def count_kmers_numpy(seq: str, k: int) -> dict[str, int]:
    """Same result again, but vectorised with NumPy (no Python loop over the positions).

    Idea: encode A, C, G, T as 0..3 (``np.frombuffer(seq.encode(), dtype=np.uint8)`` + a lookup table), build for every
    position the base-4 number of its k-mer ``sum(code[i + j] * 4 ** (k - 1 - j))``, count with ``np.bincount``, and decode
    the non-zero entries back to strings. Only k-mers that occur appear in the result.
    """
    raise NotImplementedError

def gc_content(seq: str) -> float:
    """Fraction of bases that are G or C (``0.0`` for an empty string)."""
    raise NotImplementedError

def reverse_complement(seq: str) -> str:
    """The reverse complement strand: reverse the sequence and swap A<->T, C<->G. ``reverse_complement("AACG") == "CGTT"``."""
    raise NotImplementedError

def frequencies(counts: dict[str, int]) -> dict[str, float]:
    """Normalise counts to relative frequencies that sum to 1 (empty input -> ``{}``)."""
    raise NotImplementedError

def best_time(func: Callable, *args, repeat: int=3) -> float:
    """Smallest wall-clock time (seconds, ``time.perf_counter``) of ``repeat`` calls of ``func(*args)``."""
    raise NotImplementedError

def extrapolate_hours(seconds: float, n_measured: int, n_target: int=HUMAN_GENOME_BASES) -> float:
    """Assuming linear growth, how many *hours* would ``n_target`` bases take if ``n_measured`` bases took ``seconds``?"""
    raise NotImplementedError

def compare_implementations(n: int=200000, k: int=3) -> dict[str, float]:
    """Time the three implementations on ``random_dna(n)`` and return ``{"naive": s, "counter": s, "numpy": s}``."""
    raise NotImplementedError
