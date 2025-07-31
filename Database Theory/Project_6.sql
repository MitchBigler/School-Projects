--  1. Find the most rented film title.
SELECT f.title
FROM rental r
JOIN inventory i ON r.inventory_id = i.inventory_id
JOIN film f ON i.film_id = f.film_id
GROUP BY f.film_id, f.title
ORDER BY COUNT(*) DESC
LIMIT 1;

--  2. Get customers who have rented films for more than 5 days.
SELECT DISTINCT c.first_name, c.last_name
FROM rental r
JOIN customer c ON r.customer_id = c.customer_id
WHERE r.return_date IS NOT NULL
	AND DATEDIFF(r.return_date, r.rental_date) > 5;

--  3. List all films that have never been rented.
SELECT f.title
FROM film f
LEFT JOIN inventory i ON i.film_id = f.film_id
LEFT JOIN rental r ON i.inventory_id = r.inventory_id
WHERE r.rental_id IS NULL;

--  4. Find the first and last rental dates for each customer.
SELECT c.first_name, c.last_name, MIN(r.rental_date) AS first_rental, MAX(r.rental_date) AS last_rental
FROM customer c
JOIN rental r ON r.customer_id = c.customer_id
GROUP BY c.customer_id;

--  5. Retrieve customers who rented movies in a specific category (e.g., 'Action')
SELECT c.first_name, c.last_name
FROM customer c
JOIN rental r ON c.customer_id = r.customer_id
JOIN inventory i ON r.inventory_id = i.inventory_id
JOIN film_category fc ON i.film_id = fc.film_id
JOIN category cat ON fc.category_id = cat.category_id
WHERE cat.name = 'Action';

--  6. Calculate the total number of rentals per film.
SELECT f.title, COUNT(r.rental_id) AS total_rentals
FROM film f
JOIN inventory i ON f.film_id = i.film_id
LEFT JOIN rental r ON i.inventory_id = r.inventory_id
GROUP BY f.film_id, f.title
ORDER BY total_rentals DESC;

--  7. Count the total number of films in each category.
SELECT cat.category_id, cat.name, COUNT(fc.film_id) AS film_count
FROM category cat
JOIN film_category fc ON cat.category_id = fc.category_id
GROUP BY cat.category_id, cat.name;

--  8. Find the maximum rental duration among films in each category.
SELECT cat.category_id, cat.name, MAX(f.rental_duration) AS max_rental_duration
FROM category cat
JOIN film_category fc ON cat.category_id = fc.category_id
JOIN film f ON fc.film_id = f.film_id
GROUP BY cat.category_id, cat.name;

--  9. Get the total income per store in 2005.
SELECT s.store_id, SUM(p.amount) AS total_income_2005
FROM store s
JOIN inventory i ON s.store_id = i.store_id
JOIN rental r ON i.inventory_id = r.inventory_id
JOIN payment p ON r.rental_id = p.rental_id
WHERE YEAR(p.payment_date) = 2005
GROUP BY s.store_id;

-- 10. Count the number of rentals each year.
SELECT YEAR(rental_date) AS rental_year, COUNT(*) AS total_rentals
FROM rental
GROUP BY rental_year
ORDER BY rental_year;

-- 11. Get the category with the highest average rental rate.
SELECT cat.name, AVG(f.rental_rate) AS avg_rental_rate
FROM category cat
JOIN film_category fc ON cat.category_id = fc.category_id
JOIN film f on f.film_id = fc.film_id
GROUP BY cat.category_id, cat.name
ORDER BY avg_rental_rate
LIMIT 1;

-- 12. Find the average amount spent on films per customer.
SELECT c.first_name, c.last_name, AVG(p.amount) AS avg_spend
FROM customer c
JOIN payment p ON c.customer_id = p.customer_id
GROUP BY c.customer_id;

-- 13. Determine the number of films in each store.
SELECT s.store_id, COUNT(i.film_id) AS film_count
FROM store s
JOIN inventory i on s.store_id = i.store_id
GROUP BY s.store_id;

-- 14. Find the total income for each customer.
SELECT c.first_name, c.last_name, SUM(p.amount) AS total_income
FROM customer c
JOIN payment p ON c.customer_id = p.customer_id
GROUP BY c.customer_id;

-- 15. Find the store with the highest number of films available.
SELECT s.store_id, COUNT(i.film_id) AS film_count
FROM store s
JOIN inventory i on s.store_id = i.store_id
GROUP BY s.store_id 
ORDER BY film_count DESC
LIMIT 1;

-- 16. Get the film titles in a category with an average rental rate below $3.00.
SELECT f.title, AVG(f.rental_rate) AS avg_rental_rate
FROM film f
JOIN film_category fc ON f.film_id = fc.film_id
JOIN category cat on cat.category_id = fc.category_id
GROUP BY f.film_id, f.title, cat.category_id
HAVING AVG(f.rental_rate) < 3.00
ORDER BY f.rental_rate DESC;

-- 17. List the names of customers who rented a film longer than the average rental duration.
SELECT DISTINCT c.first_name, c.last_name
FROM customer c
JOIN rental r ON c.customer_id = r.customer_id
JOIN inventory i ON r.inventory_id = i.inventory_id
JOIN film f ON i.film_id = f.film_id
WHERE f.rental_duration > (
	SELECT AVG(rental_duration)
    FROM film
	);

-- 18. Get all films that have a rating higher than the average rating.
SELECT f.title, f.rating
FROM film f
WHERE f.rating > (
	SELECT AVG(rating)
    FROM film);
    
-- 19. Find the customer who has made the most payments.
SELECT c.first_name, c.last_name, COUNT(p.payment_id) AS payment_count
FROM customer c
JOIN payment p ON c.customer_id = p.customer_id
GROUP BY c.customer_id
ORDER BY payment_count DESC
LIMIT 1;

-- 20. List the top 10 movies in 2005 (Use: Rank)
SELECT *
FROM (
	SELECT f.title, COUNT(r.rental_id) AS rentals, RANK() OVER (ORDER BY COUNT(r.rental_id) DESC) AS rank_pos
	FROM rental r
	JOIN inventory i ON r.inventory_id = i.inventory_id
	JOIN film f ON i.film_id = f.film_id
	WHERE YEAR(r.rental_date) = 2005
	GROUP BY f.film_id
) AS ranked_films
WHERE rank_pos <= 10
ORDER BY rank_pos
LIMIT 10;