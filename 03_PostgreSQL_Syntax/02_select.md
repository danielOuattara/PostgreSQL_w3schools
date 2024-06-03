# PostgreSQL Select Data

##  Select Data

To retrieve data from a data base, we use the `SELECT` statement.

##  Specify Columns

By specifying the column names, we can choose which columns to select:

```sql
SELECT customer_name, country FROM customers;
```

##  Return ALL Columns

Specify a `*` instead of the column names to select all columns:

```sql
SELECT* FROM customers;
```
