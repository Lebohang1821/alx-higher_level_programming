-- It dis 3 cities with highest average

SELECT city, ROUND(AVG(CAST(value AS DECIMAL)), 2) AS avg_temp
FROM temperatures
WHERE month IN (7, 8)
GROUP BY city
ORDER BY avg_temp DESC
LIMIT 3;
