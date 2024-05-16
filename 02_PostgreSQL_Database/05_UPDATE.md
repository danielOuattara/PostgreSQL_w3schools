# PostgreSQL UPDATE

## The UPDATE Statement

The `UPDATE` statement is used to modify the value(s)
in existing records in a table.

**Set the color of the Volvo to 'red':**

```sql
UPDATE cars
SET color = 'red'
WHERE brand = 'Volvo';
```

Result :

```sql
UPDATE 1
```

Which means that 1 row was affected by the UPDATE statement.

**Note: Be careful with the `WHERE` clause, in the example above ALL rows where brand = 'Volvo' gets updated.**

## Display Table

To check the result we can display the table with this SQL statement:

```sql
SELECT * FROM cars;
```

##  Warning! Remember WHERE

Be careful when updating records. If you omit the WHERE clause,
ALL records will be updated!

```sql
UPDATE cars
SET color = 'red';
Result
UPDATE 4
```

Which means that all 4 row was affected by the UPDATE statement.

## Update Multiple Columns

To update more than one column, separate the name/value pairs
with a comma ,:

**Update color and year for the Toyota:**

```sql
UPDATE cars
SET color = 'white', year = 1970
WHERE brand = 'Toyota';
Result
UPDATE 1
```

Which means that 1 row was affected by the UPDATE statement.

```sql
SELECT * FROM cars;
```
