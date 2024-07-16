""" Alter the Table adding a Primary Key """

from psycopg2 import OperationalError, DatabaseError
from connection_tools_v2.database import Database, DatabaseConnectionError


try:
    with Database() as connection:
        # Create a cursor object
        cursor = connection.cursor()

        # Add a new column
        cursor.execute("""
            ALTER TABLE customers
            ADD COLUMN id SERIAL PRIMARY KEY;
        """)

        connection.commit()
        print("Primary key column 'id' added successfully.")

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
