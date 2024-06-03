# PostgreSQL WHERE - Filter Data

##  Filter Records

The `WHERE` clause is used to filter records.

It is used to extract only those records that fulfill a specified
condition.

If we want to return only the records where `city` is `London`,
we can specify that in the `WHERE` clause:

```sql
SELECT * 
    FROM customers
    WHERE city = 'London';
```

## Text Fields vs. Numeric Fields

PostgreSQL requires quotes around text values.

However, numeric fields should not be enclosed in quotes:

```sql
SELECT * 
    FROM customers
    WHERE customer_id = 19;
```

```text
Note:
------

Quotes around numeric fields will not fail, but it is 
good practice to always write numeric values without quotes.
```

##  Greater than

Use the `>` operator to return all records where `customer_id`
is greater than 80:

```sql
SELECT * 
    FROM customers
    WHERE customer_id > 80;
```

```text
Note:
------

Quotes around numeric fields will not fail, but it is 
good practice to always write numeric values without quotes.
```
