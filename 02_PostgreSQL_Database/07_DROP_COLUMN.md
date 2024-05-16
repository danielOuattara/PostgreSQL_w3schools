#  PostgreSQL DROP COLUMN

## The ALTER TABLE Statement

To remove a column from a table, we have to use
the `ALTER TABLE` statement.

The `ALTER TABLE` statement is used to `add`, `delete`,
or `modify` columns in an existing table.

The `ALTER TABLE` statement is also used to `add` and `drop` various constraints on an existing table.

##  DROP COLUMN

We want to remove the column named `color` from the cars table.

To remove a column, use the `DROP COLUMN` statement:

```sql
ALTER TABLE cars
DROP COLUMN color;
```

Result

```sql
ALTER TABLE
```

##  Display Table

To check the result we can display the table with this SQL
statement:

```sql
SELECT * FROM cars;
```

```sh
\d cars
```

As you can see in the result, the color column has been removed
from the cars table.
