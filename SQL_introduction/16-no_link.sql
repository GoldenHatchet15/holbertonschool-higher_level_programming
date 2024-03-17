-- List all records from second_table with a name value, ordered by descending score
SELECT score, name 
FROM second_table 
WHERE name IS NOT NULL 
ORDER BY score DESC;
