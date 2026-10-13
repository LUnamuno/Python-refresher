-- Tables and example data from the task statement.
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

insert into teams (team_id, team_name) values
    (10, 'Give'),
    (20, 'Never'),
    (30, 'You'),
    (40, 'Up'),
    (50, 'Gonna');

insert into matches (match_id, host_team, guest_team, host_goals, guest_goals) values
    (1, 30, 20, 1, 0),
    (2, 10, 20, 1, 2),
    (3, 20, 50, 2, 2),
    (4, 10, 30, 1, 0),
    (5, 30, 50, 0, 1);
