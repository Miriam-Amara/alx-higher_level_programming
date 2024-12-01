-- host: localhost  database: hbtn_0d_tvshows
/*
lists all shows without the genre Comedy in the database hbtn_0d_tvshows.

- The tv_genres table contains only one record where name = Comedy (but the id can be different)
- Each record should display: tv_shows.title
- Results must be sorted in ascending order by the show title
- Use a maximum of two SELECT statement
- The database name will be passed as an argument of the mysql command
*/


SELECT title
FROM tv_shows
WHERE title NOT IN (SELECT s.title
                    FROM tv_genres AS g
                    LEFT JOIN
                        tv_show_genres AS sg ON g.id = sg.genre_id
                    LEFT JOIN
                        tv_shows AS s ON sg.show_id = s.id
                    WHERE g.name = "Comedy"
                )
ORDER BY title;
