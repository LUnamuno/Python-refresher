# Project 01 - Expense tracker (CLI)

A small command-line tool that stores expenses in a JSON file and prints reports.

**Skills:** dataclasses and validation, OOP, `pathlib`, `json`, `datetime`, `argparse`, exit codes, `collections`/sorting.
**Notebooks to review first:** 02 (functions), 03 (modules, I/O, stdlib), 05 (OOP).

## How to work

1. Open `expense_tracker.py`. Every function with `raise NotImplementedError` is yours to write; the docstrings are the specification.
2. Run the tests: `python -m pytest projects/01_expense_tracker -q`. Skipped tests are the ones you have not implemented yet. The goal is zero skips and zero failures.
3. Follow the milestones below in order.

## Milestones

1. `Expense` - validation in `__post_init__`, `to_dict` / `from_dict`.
2. `ExpenseStore` - load, save, `add`, `all`, `remove`.
3. Queries - `between`, `total`, `by_category`, `monthly_totals`.
4. CLI - `build_parser` and `main`.

## Try it

```powershell
python projects/01_expense_tracker/expense_tracker.py --file demo.json add 12.5 food --note "lunch"
python projects/01_expense_tracker/expense_tracker.py --file demo.json list
python projects/01_expense_tracker/expense_tracker.py --file demo.json report
```

## Stretch goals

- Add a `--month YYYY-MM` filter to `list` and `report`.
- Export a CSV file (`csv` module) and import it back.
- Add monthly budgets per category and warn when they are exceeded.
- Type-check with `mypy`, lint with `flake8`, format with `black` (see notebook 11).
