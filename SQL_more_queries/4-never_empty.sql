-- Creates the id_not_null table with an id that defaults to 1
-- and cannot be null,
-- and a name column
CREATE TABLE IF NOT EXISTS id_not_null (
  id INT NOT NULL DEFAULT 1,
  name VARCHAR(256)
);
