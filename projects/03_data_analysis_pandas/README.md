# Project 03 - Sales data analysis with pandas

Clean a messy sales table and answer business questions with `groupby`, resampling and rolling windows.

**Skills:** pandas (cleaning, dtypes, `groupby`, `resample`, `rolling`, `dt` accessor), vectorised thinking, matplotlib for the final plots.
**Notebooks to review first:** 08 (pandas), 07 (matplotlib).

## How to work

1. Open `sales_analysis.py`; `make_dataset` generates the (dirty, reproducible) data and is provided.
2. Look at the data first: `df = make_dataset(); df.info(); df.head()`.
3. `python -m pytest projects/03_data_analysis_pandas -q` (skipped = not implemented yet).

## Milestones

1. `clean` - duplicates, missing values, wrong dtypes, normalised text.
2. Aggregations - `monthly_revenue`, `top_customers`, `category_share`.
3. Time series - `daily_with_rolling`, `weekday_profile`.

## Stretch goals

- Plot monthly revenue and the rolling average in one figure with labelled axes.
- Add a cohort analysis (first purchase month vs later months).
- Write the cleaned data to Parquet/CSV and reload it checking the dtypes survive.
- Re-implement one function without `groupby` (plain Python) and compare speed.

Note: this refresher uses pandas 3 (copy-on-write, `str` dtype). Avoid chained assignment, as in notebook 08.
