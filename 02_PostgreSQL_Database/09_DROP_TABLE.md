# PostgreSQL DROP TABLE

##  The DROP TABLE Statement

The `DROP TABLE` statement is used to drop an existing table in a
database.

**Note:**

- Be careful before dropping a table.
- Deleting a table will result in loss of all information stored
  in the table!

**The following SQL statement drops the existing table cars:**

```sql
DROP TABLE cars;
```

Result

```sql
DROP TABLE
```

To check the result we can display the table with this SQL
statement:

```sql
SELECT * FROM cars;
```

Which will result in an error, because the cars table no longer exists:
Result

```sql
ERROR: relation "cars" does not exist
LINE 1: SELECT * FROM cars;
                      ^
```
