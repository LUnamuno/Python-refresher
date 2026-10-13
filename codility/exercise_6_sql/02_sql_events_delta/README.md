# 02 - SqlEventsDelta

**Codility:** [SqlEventsDelta](https://app.codility.com/programmers/trainings/6/sql_events_delta/) - Exercise 6, SQL - *easy*

Compute the difference between the latest and the second latest value for each event type.

## Task description

Given a table `events` with the following structure:

```sql
create table events (
    event_type integer not null,
    value integer not null,
    time timestamp not null,
    unique(event_type, time)
);
```

write an SQL query that, for each `event_type` that has been registered more than once, returns the difference between the latest (i.e. the most recent in terms of time) and the second latest value. The table should be ordered by `event_type` (in ascending order).

For example, given the following data:

```
 event_type | value | time
------------+-------+---------------------
 2          | 5     | 2015-05-09 12:42:00
 4          | -42   | 2015-05-09 13:19:57
 2          | 2     | 2015-05-09 14:48:30
 2          | 7     | 2015-05-09 12:54:39
 3          | 16    | 2015-05-09 13:19:57
 3          | 20    | 2015-05-09 15:01:09
```

your query should return the following rowset:

```
 event_type | value
------------+-------
 2          | -5
 3          | 4
```

For `event_type` 2, the latest value is 2 and the second latest value is 7, so the difference between them is -5.

The names of the columns in the rowset don't matter, but their order does.

Language: SQL (PostgreSQL or SQLite, selectable in Codility).

## Files

| File                    | Purpose                                                                 |
|-------------------------|-------------------------------------------------------------------------|
| `README.md`             | This description.                                                       |
| `requirements.txt`      | Dependencies of this mini-project (only Jupyter; SQLite ships with Python). |
| `setup.sql`             | `create table` + the example data of the statement.                     |
| `solution.sql`          | The solution: the query to paste into Codility.                         |
| `sql_events_delta.ipynb`| Runs the solution on SQLite, checks edge cases and compares it with a Python reference on random data. |

## How to work

```powershell
# from the repository root
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r codility/exercise_6_sql/02_sql_events_delta/requirements.txt
jupyter lab codility/exercise_6_sql/02_sql_events_delta/sql_events_delta.ipynb
```

Any SQL client works too: run `setup.sql`, then `solution.sql`.

## Hints

1. "Latest" and "second latest" suggest **ranking** the rows of each `event_type` by `time` descending: `ROW_NUMBER() OVER (PARTITION BY event_type ORDER BY time DESC)`.
2. Keep only ranks 1 and 2. Event types with a single row have only rank 1, so they disappear with `HAVING COUNT(*) = 2`.
3. The difference `latest - second latest` can be written as one aggregate: `SUM(CASE WHEN rn = 1 THEN value ELSE -value END)`.
4. Alternative without window functions: a self-join or correlated subqueries that pick the `MAX(time)` and then the maximum time below it. It works, but it is longer and easier to get wrong.
5. `unique(event_type, time)` guarantees there are no ties for "latest".
