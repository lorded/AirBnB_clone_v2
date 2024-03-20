-- Create MySQL test database for the project
CREATE DATABASE IF NOT EXISTS hbnb_test_db;

-- Create MySQL test user for the project
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';

-- Grant all privileges on the test database to the test user
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';

-- Grant select privileges on performance_schema to the test user
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';

