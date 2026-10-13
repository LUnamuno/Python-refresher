-- Table and example data from the task statement.
create table events (
    event_type integer not null,
    value integer not null,
    time timestamp not null,
    unique(event_type, time)
);

insert into events (event_type, value, time) values
    (2,   5, '2015-05-09 12:42:00'),
    (4, -42, '2015-05-09 13:19:57'),
    (2,   2, '2015-05-09 14:48:30'),
    (2,   7, '2015-05-09 12:54:39'),
    (3,  16, '2015-05-09 13:19:57'),
    (3,  20, '2015-05-09 15:01:09');
