"""Small helpers shared by the Codility tests."""

import time


def assert_fast(func, *args, limit=2.0):
    """Call ``func(*args)``, fail if it takes longer than ``limit`` seconds, return the result.

    The limits are generous (a correct solution needs a few milliseconds to a
    fraction of a second); a solution with the wrong complexity needs minutes.
    """
    start = time.perf_counter()
    result = func(*args)
    elapsed = time.perf_counter() - start
    assert elapsed < limit, f"{func.__name__} took {elapsed:.2f}s (limit {limit}s) - check the time complexity"
    return result
