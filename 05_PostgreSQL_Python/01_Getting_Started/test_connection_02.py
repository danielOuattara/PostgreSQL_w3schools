import psycopg2
from psycopg2 import OperationalError, DatabaseError
import os

# Import the connecting function from the specified module
from connection_tools_v1.connecting import connecting


try:

    connection = connecting()

    print(f'Connection established: {connection}')

    # Create a cursor object
    cursor = connection.cursor()

    # Close the connection
    cursor.close()
    connection.close()

except OperationalError as e:
    print(f"Operational error while connecting to PostgreSQL: {e}")

except DatabaseError as e:
    print(f"Database error: {e}")

finally:
    # Close the cursor and connection if they were established
    if 'cursor' in locals() and not cursor.closed:
        cursor.close()
        print("Cursor closed.")
    if 'connection' in locals() and connection and not connection.closed:
        connection.close()
        print("PostgreSQL connection is closed.")
