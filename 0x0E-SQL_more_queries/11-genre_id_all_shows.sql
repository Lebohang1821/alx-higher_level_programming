-- It lists * shows contained in database hbtn_0d_tvshows
-- If a show doesn’t have a genre, display NULL
-- You can use only one SELECT statement

SELECT s.`title`, g.`genre_id`
  FROM `tv_shows` AS s
       LEFT JOIN `tv_show_genres` AS g
       ON s.`id` = g.`show_id`
 ORDER BY s.`title`, g.`genre_id`;
