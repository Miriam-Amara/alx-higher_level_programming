-- Host: localhost  Database: hbtn_0d_tvshows
-- lists all shows contained in hbtn_0d_tvshows
-- that have at least one genre linked.

SELECT title, genre_id
FROM tv_show_genres AS tsg
LEFT JOIN tv_shows AS ts
ON tsg.show_id = ts.id
LEFT JOIN tv_genres AS tg
ON tsg.genre_id = tg.id
ORDER BY ts.title, tsg.genre_id;
