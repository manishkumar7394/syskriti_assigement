-- SQL200 – WorkSheet (Questions on Sakila database)

-- Q1 — Film prices
-- From film, show: film_id, title, rental_rate
-- Get only the films where rental_rate is 9.99 or 4.99.
select film_id,title,rental_rate			-- method 1 
from film									-- total 1000 rows
where rental_rate = 9.99 or 
rental_rate = 4.99;

select film_id, title, rental_rate			-- method 2 
from film									-- tatal 1000 rows
where rental_rate IN (9.99, 4.99);


-- Q2 — Film length + rating
-- From film, show: title, length, rating
-- Find films that are 90 to 120 minutes (inclusive) and rating is PG or PG-13.
	-- method 1
select title, length, rating
from film
where length between 90 and 120
and rating in ('PG', 'PG-13');
-- method 2
select title, length, rating from film  where length >= 90 
and length <= 120
and (rating = 'PG' or rating = 'PG-13');

-- Q3 — Actor last names
-- From actor, show: actor_id, first_name, last_name
-- Find actors whose last_name starts with S OR ends with N.
select actor_id, first_name, last_name
from actor
where last_name like 'S%'
or last_name like '%N'; 				-- output = 196 rows

-- Q4 — Active customers + email filter
-- From customer, show: customer_id, first_name, last_name, email
-- Find active customers whose email contains “.org” OR “.net”.

select customer_id, first_name, last_name, email
from customer
where active = 1
and (
      email like '%.org%'
      or email like '%.net%'
    );								-- output = 599 rows
    
-- Q5 — Inactive customers in store 1
-- From customer, show: customer_id, store_id, active
-- Find customers from store 1 who are not active.
select customer_id, store_id, active 
from customer
where store_id = 1 and active =0; 

-- Q6 — Payment amount + date range
-- From payment, show: payment_id, customer_id, amount, payment_date
-- Find payments with amount between 2.00 and 5.00 and made in February 2007.

select payment_id, customer_id, amount, payment_date
from payment
where amount between 2.00 and 5.00
and payment_date >= '2007-02-01'
and payment_date < '2007-03-01'; 		-- output 0 

-- Q7 — Rentals not returned
-- From rental, show: rental_id, rental_date, return_date, customer_id
-- Find rentals where return_date is NULL.
select rental_id, rental_date, return_date, customer_id
from rental
where return_date is null;
-- Q8 — Address district + postal code present
-- From address, show: address_id, address, district, postal_code
-- Find addresses where district is Texas or California AND postal_code is not NULL.
select address_id, address, district, postal_code
from address
where district in ('Texas', 'California')
and postal_code is not null;

-- Q9 — Replacement cost + exclude titles
-- From film, show: film_id, title, replacement_cost
-- Find films where replacement_cost is 12.99, 16.99, or 28.99
-- AND the title does NOT contain the letter A.
select film_id, title, replacement_cost
from film
where replacement_cost in (12.99, 16.99, 28.99)
and title not like '%A%';

-- Q10 — Inventory logic challenge
-- From inventory, show: inventory_id, film_id, store_id
-- Find inventory items where:
-- • (store_id = 1 AND film_id between 1 and 50)
-- OR
-- • (store_id = 2 AND film_id between 51 and 100)

select inventory_id, film_id, store_id
from inventory
where 
(
    store_id = 1 
    and film_id between 1 and 50
)
or
(
    store_id = 2 
    and film_id between 51 and 100			-- output = 456 rows
);





