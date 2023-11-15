-- It lists all shows, and all genres linked
-- to that show, from the database hbtn_0d_tvshows
-- If a show doesn’t have a genre, display NULL in genre column

SELECT t.`title`
  FROM `tv_shows` AS t
       INNER JOIN `tv_show_genres` AS s
       ON t.`id` = s.`show_id`

       INNER JOIN `tv_genres` AS g
       ON g.`id` = s.`genre_id`
       WHERE g.`name` = "Comedy"
 ORDER BY t.`title`;
