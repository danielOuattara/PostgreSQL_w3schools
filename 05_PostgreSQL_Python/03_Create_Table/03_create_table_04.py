""" Alter the Table adding a Primary Key """

from psycopg2 import OperationalError, DatabaseError
from connection_tools_v2.database import Database, DatabaseConnectionError


try:
    with Database() as connection:
        # Create a cursor object
        cursor = connection.cursor()

        # Check if the column has unique values and is not null
        cursor.execute("""
            SELECT COUNT(DISTINCT id) = COUNT(id) AS is_unique
            FROM customers_3;
        """)
        is_unique = cursor.fetchone()[0]

        if is_unique:
            # Add primary key constraint
            cursor.execute("""
                ALTER TABLE customers_3
                ADD PRIMARY KEY (id);
            """)

            print(f"Column 'id' set as primary key.")

        else:
            print("Column 'id' does not have unique values or contains nulls. "
                  "Ensure uniqueness and non-null values before setting as primary key.")

        connection.commit()
        print("Table 'customers_3' updated successfully")

except DatabaseConnectionError as e:
    print(f"Error: {e}")

except OperationalError as e:
    print(f"Operational error: {e}")

except DatabaseError as e:
    print(f"Database error: {e}")

finally:
    if 'cursor' in locals() and not cursor.closed:
        cursor.close()
        print("Cursor closed.")
