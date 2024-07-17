""" from psycopg2 import OperationalError, DatabaseError
from connection_tools_v2.database import Database, DatabaseConnectionError

try:
    with Database() as connection:
        # Create a cursor object
        cursor = connection.cursor()

        # Your query logic here

        # Close the cursor
        cursor.close()
        print("Cursor closed.")

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
 """

import sys
import os
from psycopg2 import OperationalError, DatabaseError

# Add the parent directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from connection_tools_v2.database import Database, DatabaseConnectionError

try:
    with Database() as connection:
        # Create a cursor object
        cursor = connection.cursor()

        # Your query logic here

        # Close the cursor
        cursor.close()
        print("Cursor closed.")

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
