# 01 - SqlSum

**Codility:** [SqlSum](https://app.codility.com/programmers/trainings/6/sql_sum/) - Exercise 6, SQL - *elementary*

Calculate the sum of elements.

## Task description

Given a table `elements` with the following structure:

```sql
create table elements (
    v integer not null
);
```

write an SQL query that returns the sum of the numbers in column `v`.

For example, given:

```
 v
---
 2
 10
 20
 10
```

your query should return `42`.

Language: SQL (PostgreSQL or SQLite, selectable in Codility).

## Files

| File               | Purpose                                                                 |
|--------------------|-------------------------------------------------------------------------|
| `README.md`        | This description.                                                       |
| `requirements.txt` | Dependencies of this mini-project (only Jupyter; SQLite ships with Python). |
| `setup.sql`        | `create table` + the example data of the statement.                     |
| `solution.sql`     | The solution: the query to paste into Codility.                         |
| `sql_sum.ipynb`    | Loads `setup.sql` into an in-memory SQLite database, runs `solution.sql` and checks it. |

## How to work

```powershell
# from the repository root
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r codility/exercise_6_sql/01_sql_sum/requirements.txt
jupyter lab codility/exercise_6_sql/01_sql_sum/sql_sum.ipynb
```

Any SQL client works too: run `setup.sql`, then `solution.sql`.

## Hints

1. `SUM(column)` is an aggregate function: with no `GROUP BY` it collapses the whole table into one row.
2. `SUM` over zero rows returns `NULL`, not `0`. Wrap it in `COALESCE(SUM(v), 0)` if you want `0` for an empty table.
3. Related aggregates worth knowing: `COUNT`, `AVG`, `MIN`, `MAX`.
