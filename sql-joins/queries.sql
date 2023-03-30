-- write your queries here
SELECT * FROM owners LEFT JOIN vehicles ON vehicles.owner_id = owners.id;
SELECT o.first_name, o.last_name, count(*) as count FROM owners o JOIN vehicles v ON v.owner_id = o.id GROUP BY o.first_name, o.last_name ORDER BY first_name ASC;
SELECT o.first_name, o.last_name, avg(price) as average_price, count(*) as count FROM owners o JOIN vehicles v ON v.owner_id = o.id GROUP BY o.first_name, o.last_name HAVING avg(price) > 10000 ORDER BY first_name DESC;