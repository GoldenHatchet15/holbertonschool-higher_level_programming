-- Create the database if it doesn't already exist
-- Grant the SELECT privilege to the user specifically for the new database
-- Create the user if they don't already exist and set their password

CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';
