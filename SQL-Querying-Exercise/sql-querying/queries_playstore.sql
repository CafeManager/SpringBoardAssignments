-- Comments in SQL Start with dash-dash --
--(app_name, category, rating, reviews, size, min_installs, price, content_rating, genres, last_updated, current_version, android_version)--
    SELECT * FROM analytics WHERE ID = 1880;
    SELECT ID, APP_NAME FROM analytics WHERE last_updated = 'August 01, 2018';
    SELECT category, COUNT(*) FROM analytics GROUP BY category;
    SELECT app_name, reviews FROM analytics ORDER BY reviews DESC LIMIT 5;
    SELECT app_name, reviews, rating FROM analytics WHERE rating >= 4.8 ORDER BY REVIEWS DESC LIMIT 1;
    SELECT category, AVG(rating) as rating FROM analytics GROUP BY category ORDER BY rating DESC;
    SELECT app_name, min_installs, rating FROM analytics WHERE min_installs <= 50 AND rating IS NOT NULL ORDER BY rating DESC;
    SELECT app_name, rating, reviews FROM analytics WHERE rating < 3 AND reviews >= 10000;
    SELECT app_name, reviews, price FROM analytics WHERE price BETWEEN .10 AND 1.00 ORDER BY reviews DESC LIMIT 10;
    SELECT app_name, last_updated FROM analytics ORDER BY last_updated LIMIT 1; 
    SELECT app_name, last_updated FROM analytics ORDER BY last_updated DESC LIMIT 1; 
    SELECT SUM(reviews) FROM analytics;
    SELECT category, SUM(reviews) FROM analytics GROUP BY category HAVING count(*) > 300;
    SELECT app_name, reviews, min_installs, min_installs/reviews AS proportion FROM analytics WHERE min_installs >= 100000 ORDER BY  proportion DESC LIMIT 1;