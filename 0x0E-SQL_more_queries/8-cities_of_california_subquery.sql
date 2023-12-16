-- It lists * cities of CA in database hbtn_0d_usa
-- You are not allowed to use JOIN keyword

SELECT `id`, `name`
  FROM `cities`
 WHERE `state_id` IN
       (SELECT `id`
	  FROM `states`
	 WHERE `name` = "California")
 ORDER BY `id`;
