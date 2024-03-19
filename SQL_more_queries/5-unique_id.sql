-- Creates the unique_id table with a unique id
-- that defaults to 1, and a name column
CREATE TABLE IF NOT EXISTS unique_id (
  id INT NOT NULL DEFAULT 1 UNIQUE,
  name VARCHAR(256)
);
