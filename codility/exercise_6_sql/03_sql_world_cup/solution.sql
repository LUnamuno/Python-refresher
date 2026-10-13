-- SqlWorldCup: points per team (win = 3, draw = 1, loss = 0), including teams with no matches.
-- Ordered by num_points descending, then team_id ascending.
-- Standard SQL: works unchanged in SQLite and PostgreSQL.
with results as (
    select
        host_team as team_id,
        case
            when host_goals > guest_goals then 3
            when host_goals = guest_goals then 1
            else 0
        end as points
    from matches
    union all
    select
        guest_team as team_id,
        case
            when guest_goals > host_goals then 3
            when guest_goals = host_goals then 1
            else 0
        end as points
    from matches
)
select
    t.team_id,
    t.team_name,
    coalesce(sum(r.points), 0) as num_points
from teams t
left join results r on r.team_id = t.team_id
group by t.team_id, t.team_name
order by num_points desc, t.team_id asc;
