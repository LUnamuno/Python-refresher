-- SqlEventsDelta: for each event_type registered more than once, the latest value
-- minus the second latest value, ordered by event_type.
-- Standard SQL (CTE + window function): works in SQLite >= 3.25 and PostgreSQL.
with ranked as (
    select
        event_type,
        value,
        row_number() over (partition by event_type order by time desc) as rn
    from events
)
select
    event_type,
    sum(case when rn = 1 then value else -value end) as value
from ranked
where rn <= 2
group by event_type
having count(*) = 2
order by event_type;
