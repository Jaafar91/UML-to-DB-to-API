DROP TABLE IF EXISTS animals;
CREATE TABLE animals (
id   int NOT NULL PRIMARY KEY,
name      varchar(100),
type      varchar(100),
location  varchar(100),
date_of_birth  date
);
