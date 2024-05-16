# PostgreSQL DELETE

##  The DELETE Statement

The `DELETE` statement is used to delete existing
records in a table.

**Note:**

- Be careful when deleting records in a table!
- Notice the `WHERE` clause in the `DELETE` statement.
- The `WHERE` clause specifies which record(s) should be deleted.

If you omit the `WHERE` clause all records in the table will be
deleted!.

**To delete the record(s) where brand is 'Volvo', use this statement:**

```sql
DELETE FROM cars
WHERE brand = 'Volvo';
```

Result

```sql
DELETE 1
```

Which means that 1 row was deleted.

##  Display Table

To check the result we can display the table with this SQL statement:

```sql
SELECT * FROM cars;
```

##  Delete All Records

It is possible to delete all rows in a table without deleting the
table. This means that the table structure, attributes, and indexes
will be intact.

The following SQL statement deletes all rows in the cars table,
without deleting the table:

```sql
DELETE FROM cars;
```

Result

```sql
DELETE 3
```

Which means that all 3 rows were deleted.

To check the result we can display the table with this SQL statement:

```sql
SELECT * FROM cars;
```

## TRUNCATE TABLE

Because we omit the WHERE clause in the `DELETE` statement above,
all records will be deleted from the cars table.

The same would have been achieved by using the `TRUNCATE TABLE` statement:

```sql
TRUNCATE TABLE cars;
```

Result

```sql
TRUNCATE TABLE
```

To check the result we can display the table with this SQL statement:

```sql
SELECT * FROM cars;
```
