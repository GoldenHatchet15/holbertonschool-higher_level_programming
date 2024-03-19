-- Lists all genres and the number of shows 
-- linked to each from the hbtn_0d_tvshows database
SELECT tg.name AS genre, COUNT(tsg.show_id) AS number_of_shows
FROM tv_show_genres tsg
JOIN tv_genres tg ON tsg.genre_id = tg.id
GROUP BY tg.name
ORDER BY COUNT(tsg.show_id) DESC, tg.name;
