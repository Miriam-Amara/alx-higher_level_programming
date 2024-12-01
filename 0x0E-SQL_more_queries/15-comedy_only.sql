-- host: localhost  database: hbtn_0d_tvshows

-- lists all Comedy shows in the database hbtn_0d_tvshows.

-- The tv_genres table contains only one record where name = Comedy (but the id can be different)
-- Each record should display: tv_shows.title
-- Results must be sorted in ascending order by the show title
-- You can use only one SELECT statement
-- The database name will be passed as an argument of the mysql command



SELECT ts.title
FROM tv_genres AS tg
LEFT JOIN tv_show_genres AS tsg
ON tg.id = tsg.genre_id
LEFT JOIN tv_shows AS ts
ON tsg.show_id = ts.id
WHERE tg.name = "Comedy"
ORDER BY ts.title;
