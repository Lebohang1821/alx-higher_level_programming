-- It lists * cities contained in database hbtn_0d_usa
-- You can use only one SELECT statement

SELECT cities.id, cities.name, states.name
FROM cities
INNER JOIN states ON cities.state_id=states.id
ORDER BY cities.id;
