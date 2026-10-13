import numpy as np
import pandas as pd
import pytest

from sales_analysis import (
    category_share,
    clean,
    daily_with_rolling,
    make_dataset,
    monthly_revenue,
    top_customers,
    weekday_profile,
)


@pytest.fixture(scope="module")
def raw():
    return make_dataset()


@pytest.fixture(scope="module")
def tidy(raw):
    return clean(raw)


def test_make_dataset_is_dirty(raw):                    # PROVIDED helper: must pass from the start
    assert list(raw.columns) == ["order_id", "date", "customer", "category", "quantity", "unit_price"]
    assert raw["quantity"].isna().sum() > 0 and raw["unit_price"].isna().sum() > 0
    assert raw.duplicated().sum() == 15
    assert raw["category"].nunique() > 5


# ---------------------------------------------------------------------------------------------------- clean
def test_clean_does_not_modify_input(raw):
    before = raw.copy()
    clean(raw)
    pd.testing.assert_frame_equal(raw, before)


def test_clean_rows_and_columns(raw, tidy):
    normalised = raw.assign(category=raw["category"].str.strip().str.lower())
    expected_rows = len(normalised.drop_duplicates().dropna(subset=["unit_price"]))
    assert len(tidy) == expected_rows
    assert list(tidy.columns) == ["order_id", "date", "customer", "category", "quantity", "unit_price", "revenue"]


def test_clean_types_and_values(tidy):
    assert pd.api.types.is_datetime64_any_dtype(tidy["date"])
    assert pd.api.types.is_integer_dtype(tidy["quantity"])
    assert tidy[["quantity", "unit_price", "revenue"]].notna().all().all()
    assert sorted(tidy["category"].unique()) == ["books", "games", "garden", "kitchen", "toys"]
    assert not tidy.duplicated().any()
    assert np.allclose(tidy["revenue"], tidy["quantity"] * tidy["unit_price"])


def test_clean_sorted_with_fresh_index(tidy):
    assert list(tidy.index) == list(range(len(tidy)))
    keys = list(zip(tidy["date"], tidy["order_id"]))
    assert keys == sorted(keys)


def test_clean_fills_missing_quantity_with_one(raw, tidy):
    ids = raw.loc[raw["quantity"].isna() & raw["unit_price"].notna(), "order_id"]
    assert len(ids) > 0
    assert (tidy.loc[tidy["order_id"].isin(ids), "quantity"] == 1).all()


# ---------------------------------------------------------------------------------------------------- questions
def test_monthly_revenue(tidy):
    result = monthly_revenue(tidy)
    assert result.name == "revenue" and result.index.name == "month"
    assert list(result.index) == ["2024-01", "2024-02", "2024-03", "2024-04", "2024-05", "2024-06"]
    assert result.sum() == pytest.approx(tidy["revenue"].sum())
    jan = tidy.loc[tidy["date"].dt.month == 1, "revenue"].sum()
    assert result["2024-01"] == pytest.approx(jan)


def test_top_customers(tidy):
    top = top_customers(tidy, 3)
    assert list(top.columns) == ["customer", "revenue", "orders"]
    assert len(top) == 3 and list(top.index) == [0, 1, 2]
    assert top["revenue"].is_monotonic_decreasing
    best = tidy.groupby("customer")["revenue"].sum().idxmax()
    assert top.loc[0, "customer"] == best
    assert top.loc[0, "orders"] == (tidy["customer"] == best).sum()
    assert len(top_customers(tidy)) == 5


def test_category_share(tidy):
    share = category_share(tidy)
    assert share.name == "share"
    assert share.sum() == pytest.approx(1.0)
    assert share.is_monotonic_decreasing
    assert set(share.index) == {"books", "games", "garden", "kitchen", "toys"}


def test_daily_with_rolling(tidy):
    daily = daily_with_rolling(tidy, window=7)
    first, last = tidy["date"].min(), tidy["date"].max()
    assert list(daily.columns) == ["revenue", "rolling_mean"]
    assert len(daily) == (last - first).days + 1
    assert daily.index.is_monotonic_increasing and daily.index.to_series().diff().dropna().eq(pd.Timedelta("1D")).all()
    assert daily["revenue"].sum() == pytest.approx(tidy["revenue"].sum())
    assert daily["rolling_mean"].iloc[:6].isna().all() and daily["rolling_mean"].iloc[6:].notna().all()
    assert daily["rolling_mean"].iloc[10] == pytest.approx(daily["revenue"].iloc[4:11].mean())


def test_weekday_profile(tidy):
    profile = weekday_profile(tidy)
    order = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    assert list(profile.index) == order
    monday = tidy.loc[tidy["date"].dt.dayofweek == 0, "revenue"].mean()
    assert profile["Monday"] == pytest.approx(monday)
