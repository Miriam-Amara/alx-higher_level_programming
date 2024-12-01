-- host: localhost  database: hbtn_0d_tvshows_rate

-- lists all genres in the database hbtn_0d_tvshows_rate by their rating.

-- Each record should display: tv_genres.name - rating sum
-- Results must be sorted in descending order by their rating
-- Use only one SELECT statement
-- The database name will be passed as an argument of the mysql command



SELECT g.name, SUM(rate) AS rating
FROM tv_show_ratings AS sr
LEFT JOIN 
    tv_show_genres AS sg USING(show_id)
LEFT JOIN
    tv_genres AS g ON sg.genre_id = g.id
WHERE g.name IS NOT NULL
GROUP BY g.name
ORDER BY rating DESC;
