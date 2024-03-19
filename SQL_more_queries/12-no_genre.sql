-- Lists all shows without a genre linked 
-- from the hbtn_0d_tvshows database
SELECT ts.title, tsg.genre_id
FROM tv_shows ts
LEFT JOIN tv_show_genres tsg ON ts.id = tsg.show_id
WHERE tsg.genre_id IS NULL
ORDER BY ts.title ASC;
