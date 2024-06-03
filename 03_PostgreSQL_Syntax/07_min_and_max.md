# PostgreSQL MIN and MAX Functions

## MIN

The `MIN()` function returns the smallest value of
the selected column.

> Return the lowest price in the products table:

```sql
SELECT MIN(price) FROM products;
```

## MAX

The `MAX()` function returns the largest value of
the selected column.

> Return the highest price in the products table:

```sql
SELECT MAX(price) FROM products;
```

##  Set Column Name

When you use `MIN()` or `MAX()`, the returned column
will be named `min` or `max` by default.

To give the column a new name, use the `AS` keyword.

> Return the lowest price, and name the column lowest_price:

```sql
SELECT MIN(price) AS lowest_price
FROM products;
```
