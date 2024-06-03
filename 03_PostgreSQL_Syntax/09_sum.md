# PostgreSQL SUM Function

##  SUM

The `SUM()` function returns the total sum of a numeric column.

The following SQL statement finds the sum of the quantity fields
in the order_details table:

> Return the total amount of ordered items:

```sql
SELECT SUM(quantity)
    FROM order_details;
```
