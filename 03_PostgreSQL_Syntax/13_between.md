# PostgreSQL BETWEEN Operator

## BETWEEN

The `BETWEEN` operator selects values within a given range.
The values can be numbers, text, or dates.

The `BETWEEN` operator is inclusive: begin and end values are included.

> Select all products with a price between 10 and 15:

```sql
SELECT * 
FROM Products
WHERE Price BETWEEN 10 AND 15;
```

## BETWEEN Text Values

The `BETWEEN` operator can also be used on text values.

The result returns all records that are alphabetically between the specified values.

> Select all products between 'Pavlova' and 'Tofu':

```sql
SELECT * 
FROM Products
WHERE product_name BETWEEN 'Pavlova' AND 'Tofu';
```

If we add an `ORDER BY` clause to the example above,
it will be a bit easier to read:

> Same example as above, but we sort it by product_name:

```sql
SELECT * 
FROM Products
WHERE product_name BETWEEN 'Pavlova' AND 'Tofu'
ORDER BY product_name;
```

##  BETWEEN Date Values

The `BETWEEN` operator can also be used on date values.

> Select all orders between 12. of April 2023 and 5. of May 2023:

```sql
SELECT * 
FROM orders
WHERE order_date BETWEEN '2023-04-12' AND '2023-05-05';


--  customers who had ordered between '2023-04-12' AND '2023-05-05'

SELECT *
FROM customers 
WHERE customer_id IN (SELECT customer_id FROM orders WHERE order_date BETWEEN '2023-04-12' AND '2023-05-05');

--  count customers who had ordered between '2023-04-12' AND '2023-05-05'

SELECT COUNT(customer_id)
FROM customers 
WHERE customer_id IN (SELECT customer_id FROM orders WHERE order_date BETWEEN '2023-04-12' AND '2023-05-05');
```
