-- host: localhost  database: hbtn_0d_tvshows

-- lists all shows, and all genres linked to that show, from the database hbtn_0d_tvshows.

-- If a show doesn’t have a genre, display NULL in the genre column
-- Each record should display: tv_shows.title - tv_genres.name
-- Results must be sorted in ascending order by the show title and genre name
-- You can use only one SELECT statement
-- The database name will be passed as an argument of the mysql command


SELECT ts.title, tg.name
FROM tv_shows AS ts
LEFT JOIN tv_show_genres AS tsg
ON ts.id = tsg.show_id
LEFT JOIN tv_genres AS tg
ON tsg.genre_id = tg.id
ORDER BY ts.title, tg.name;
