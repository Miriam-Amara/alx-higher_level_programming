-- host: localhost  database: hbtn_0d_tvshows

-- a script that uses the hbtn_0d_tvshows database to list all genres not linked to the show Dexter

-- The tv_shows table contains only one record where title = Dexter (but the id can be different)
-- Each record should display: tv_genres.name
-- Results must be sorted in ascending order by the genre name
-- You can use a maximum of two SELECT statement
-- The database name will be passed as an argument of the mysql command


SELECT name
FROM tv_genres
WHERE name NOT IN (SELECT g.name
                    FROM
                        tv_genres AS g 
                    LEFT JOIN
                        tv_show_genres AS sg ON g.id = sg.genre_id
                    LEFT JOIN
                        tv_shows AS s ON sg.show_id = s.id
                    WHERE s.title = "Dexter"
                    )
ORDER BY name;
