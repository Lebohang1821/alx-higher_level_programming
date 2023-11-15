-- It dis average temperature (in Fahrenheit)
-- City order by descending temperature

SELECT city, ROUND(AVG(value), 2) AS avg_temp
FROM temperatures
GROUP BY city
ORDER BY avg_temp DESC;
