# 03 - SqlWorldCup

**Codility:** [SqlWorldCup](https://app.codility.com/programmers/trainings/6/sql_world_cup/) - Exercise 6, SQL - *medium*

Given a list of matches in a group stage of the soccer World Cup, compute the number of points each team currently has.

## Task description

You are given two tables, `teams` and `matches`, with the following structures:

```sql
create table teams (
    team_id integer not null,
    team_name varchar(30) not null,
    unique(team_id)
);

create table matches (
    match_id integer not null,
    host_team integer not null,
    guest_team integer not null,
    host_goals integer not null,
    guest_goals integer not null,
    unique(match_id)
);
```

Each record in the table `teams` represents a single soccer team. Each record in the table `matches` represents a finished match between two teams. Teams (`host_team`, `guest_team`) are represented by their IDs in the `teams` table (`team_id`). No team plays a match against itself. You know the result of each match (that is, the number of goals scored by each team).

You would like to compute the total number of points each team has scored after all the matches described in the table. The scoring rules are as follows:

- If a team wins a match (scores strictly more goals than the other team), it receives **three** points.
- If a team draws a match (scores exactly the same number of goals as the opponent), it receives **one** point.
- If a team loses a match (scores fewer goals than the opponent), it receives **no** points.

Write an SQL query that returns a ranking of **all** teams (`team_id`) described in the table `teams`. For each team you should provide its name and the number of points it received after all described matches (`num_points`). The table should be ordered by `num_points` (in decreasing order). In case of a tie, order the rows by `team_id` (in increasing order).

For example, for:

```
teams:
 team_id | team_name
---------+-----------
 10      | Give
 20      | Never
 30      | You
 40      | Up
 50      | Gonna

matches:
 match_id | host_team | guest_team | host_goals | guest_goals
----------+-----------+------------+------------+-------------
 1        | 30        | 20         | 1          | 0
 2        | 10        | 20         | 1          | 2
 3        | 20        | 50         | 2          | 2
 4        | 10        | 30         | 1          | 0
 5        | 30        | 50         | 0          | 1
```

your query should return:

```
 team_id | team_name | num_points
---------+-----------+------------
 20      | Never     | 4
 50      | Gonna     | 4
 10      | Give      | 3
 30      | You       | 3
 40      | Up        | 0
```

Language: SQL (PostgreSQL or SQLite, selectable in Codility).

## Files

| File                  | Purpose                                                                 |
|-----------------------|-------------------------------------------------------------------------|
| `README.md`           | This description.                                                       |
| `requirements.txt`    | Dependencies of this mini-project (only Jupyter; SQLite ships with Python). |
| `setup.sql`           | `create table`s + the example data of the statement.                    |
| `solution.sql`        | The solution: the query to paste into Codility.                         |
| `sql_world_cup.ipynb` | Runs the solution on SQLite, checks edge cases and compares it with a Python reference on random data. |

## How to work

```powershell
# from the repository root
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r codility/exercise_6_sql/03_sql_world_cup/requirements.txt
jupyter lab codility/exercise_6_sql/03_sql_world_cup/sql_world_cup.ipynb
```

Any SQL client works too: run `setup.sql`, then `solution.sql`.

## Hints

1. Every match gives points to **two** teams, each seen from its own side. Turn each row of `matches` into two rows `(team_id, points)`: one for the host and one for the guest, then `UNION ALL` them.
2. `CASE WHEN goals > opponent_goals THEN 3 WHEN goals = opponent_goals THEN 1 ELSE 0 END` computes the points of one side.
3. Teams that have not played any match must still appear with `0` points: start from `teams` and `LEFT JOIN` the results, then `COALESCE(SUM(points), 0)`.
4. Use `UNION ALL`, not `UNION`: `UNION` would remove duplicate rows (e.g. two different matches that both give 3 points to the same team) and corrupt the sum.
5. Order with `ORDER BY num_points DESC, team_id ASC`.
