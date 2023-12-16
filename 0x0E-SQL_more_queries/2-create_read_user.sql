-- It creates database hbtn_0d_2 and the user user_0d_2
-- User_0d_2 password should be set - user_0d_2_pwd
-- user_0d_2 should have only SELECT privilege in database hbtn_0d_2

CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';
GRANT SELECT ON `hbtn_0d_2`.* TO 'user_0d_2'@'localhost';

-- It apply all changes
FLUSH PRIVILEGES;
