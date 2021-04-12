CREATE TABLE user (
id   int,
first_name     varchar(100),
last_name      varchar(100),
date_of_birth  date
);

CREATE TABLE group (
id   int,
code   varchar(100),
name   varchar(100)
);

CREATE TABLE user_group (
id        int,
user_id    int,
group_id   int
);
