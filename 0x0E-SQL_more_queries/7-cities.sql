-- It creates database hbtn_0d_usa and table cities
-- (in the database hbtn_0d_usa) on your MySQL server

CREATE DATABASE IF NOT EXISTS `hbtn_0d_usa`;

-- Create a table named cities within the hbtn_0d_usa database
CREATE TABLE IF NOT EXISTS `hbtn_0d_usa`.`cities` (
    -- Define the primary key for the table, which is an auto-incremented integer
    PRIMARY KEY(`id`),
    -- Define the 'id' column as an integer that cannot be NULL and auto-increments
    `id`       INT          NOT NULL AUTO_INCREMENT,
    -- Define the 'state_id' column as an integer that cannot be NULL
    `state_id` INT          NOT NULL,
    -- Define the 'name' column as a variable character string with a maximum length of 256 characters, cannot be NULL
    `name`     VARCHAR(256) NOT NULL,
    -- Create a foreign key relationship between 'state_id' in 'cities' and 'id' in 'states' table
    FOREIGN KEY(`state_id`)
    REFERENCES `hbtn_0d_usa`.`states`(`id`));
