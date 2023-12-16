-- It makes table unique_id on MySQL server
-- database name will be passed as an argument of mysql command
-- table unique_id already exists, your script should not fail

CREATE TABLE IF NOT EXISTS `unique_id` (
    `id`   INT          DEFAULT 1 UNIQUE,
    `name` VARCHAR(256));
