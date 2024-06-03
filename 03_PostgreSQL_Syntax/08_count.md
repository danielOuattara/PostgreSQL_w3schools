# PostgreSQL COUNT Function

##  COUNT

The `COUNT()` function returns the number of rows that
matches a specified criterion.

If the specified criterion is a column name, the `COUNT()`
function returns the number of columns with that name.

> Return the number of customers from the customers table:

```sql
SELECT COUNT(customer_id)
    FROM customers;
```

```text
Note: 
-----

NULL values are not counted.
```

By specifying a `WHERE` clause, you can e.g. return the
number of customers that comes from London:

> Return the number of customers from London:

```sql
SELECT COUNT(customer_id)
    FROM customers
    WHERE city = 'London';
```

> Return the number of different country from customers

```sql
SELECT COUNT( DISTINCT country) 
    FROM customers;
```
