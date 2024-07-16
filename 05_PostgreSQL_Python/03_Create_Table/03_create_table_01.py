""" Create a Table """

from psycopg2 import OperationalError, DatabaseError
from connection_tools_v2.database import Database, DatabaseConnectionError


try:
    with Database() as connection:
        # Create a cursor object
        cursor = connection.cursor()
        cursor.execute("""
            CREATE TABLE customers (
                id INT,
                name VARCHAR(255),
                address VARCHAR(255)
            )
        """)
        connection.commit()
        print("Table 'customers' created successfully")


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
