-- Import the provided table dump into hbtn_0c_0 database
-- Assuming the file is named 'table_dump.sql'
SOURCE /path/to/table_dump.sql;

-- Display the average temperature by city ordered by temperature (descending)
SELECT city, AVG(temperature) AS avg_temp
FROM temperatures
GROUP BY city
ORDER BY avg_temp DESC;

