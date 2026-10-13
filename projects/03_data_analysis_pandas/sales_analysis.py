"""Project 03 - Sales analysis with pandas: clean a messy table, then answer business questions.

``make_dataset`` (provided) generates a deliberately dirty order table. Implement the functions below, then run::

    python -m pytest projects/03_data_analysis_pandas -q

and finish with the report notebook described in the README.
"""
from __future__ import annotations
import numpy as np
import pandas as pd
CATEGORIES = ['books', 'games', 'garden', 'kitchen', 'toys']

def make_dataset(n: int=600, seed: int=42) -> pd.DataFrame:
    """PROVIDED. Dirty order table with columns ``order_id, date, customer, category, quantity, unit_price``.

    Problems on purpose: dates are *strings*; categories have random capitalisation and stray blanks;
    ~5% of ``quantity`` and ~3% of ``unit_price`` are missing; 15 rows are exact duplicates of other rows.
    """
    rng = np.random.default_rng(seed)
    dates = pd.Timestamp('2024-01-01') + pd.to_timedelta(rng.integers(0, 180, n), unit='D')
    category = rng.choice(CATEGORIES, n)
    messy = [c.upper() if r < 0.2 else ' ' + c + ' ' if r < 0.4 else c.title() for c, r in zip(category, rng.random(n))]
    quantity = rng.integers(1, 6, n).astype(float)
    quantity[rng.random(n) < 0.05] = np.nan
    price = np.round(rng.gamma(4.0, 8.0, n), 2)
    price[rng.random(n) < 0.03] = np.nan
    df = pd.DataFrame({'order_id': np.arange(1, n + 1), 'date': dates.strftime('%Y-%m-%d'), 'customer': [f'C{c:03d}' for c in rng.integers(1, 41, n)], 'category': messy, 'quantity': quantity, 'unit_price': price})
    return pd.concat([df, df.sample(15, random_state=seed)], ignore_index=True)

def clean(df: pd.DataFrame) -> pd.DataFrame:
    """Return a *new*, clean DataFrame (never modify the argument):

    1. ``category``: strip blanks and lower-case it.
    2. ``date``: convert to ``datetime64`` (``pd.to_datetime``).
    3. Drop exact duplicate rows (after step 1).
    4. Drop rows whose ``unit_price`` is missing.
    5. Fill a missing ``quantity`` with 1 and make the column an integer dtype.
    6. Add ``revenue = quantity * unit_price``.
    7. Sort by ``date`` then ``order_id`` and reset the index (``drop=True``).
    """
    raise NotImplementedError

def monthly_revenue(df: pd.DataFrame) -> pd.Series:
    """Revenue per calendar month of a *clean* table: a ``Series`` named ``"revenue"`` whose index (named ``"month"``)
    holds strings such as ``"2024-03"`` in chronological order."""
    raise NotImplementedError

def top_customers(df: pd.DataFrame, n: int=5) -> pd.DataFrame:
    """The ``n`` customers with the highest total revenue: columns ``customer, revenue, orders`` (``orders`` = number of
    rows), sorted by revenue descending, with a fresh 0..n-1 index."""
    raise NotImplementedError

def category_share(df: pd.DataFrame) -> pd.Series:
    """Share of the total revenue of each category, biggest first. A ``Series`` named ``"share"`` that sums to 1."""
    raise NotImplementedError

def daily_with_rolling(df: pd.DataFrame, window: int=7) -> pd.DataFrame:
    """Daily revenue with a trailing rolling mean.

    Index: *every* calendar day from the first to the last order (days without orders count as 0 revenue).
    Columns: ``revenue`` (that day's total) and ``rolling_mean`` (mean of the last ``window`` days, NaN until a full
    window is available).
    """
    raise NotImplementedError

def weekday_profile(df: pd.DataFrame) -> pd.Series:
    """Average revenue *per order* for each weekday, indexed by English weekday names ``Monday..Sunday`` in that order
    (days with no orders are omitted)."""
    raise NotImplementedError
