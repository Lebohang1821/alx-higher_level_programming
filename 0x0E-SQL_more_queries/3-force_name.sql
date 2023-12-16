-- It creates table force_name on your MySQL server
-- Database name will be passed as an argument of mysql command

CREATE TABLE IF NOT EXISTS `force_name` (
    `id`   INT,
    `name` VARCHAR(256) NOT NULL);
