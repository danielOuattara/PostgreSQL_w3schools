""" Check if Table Exists """
from psycopg2 import OperationalError, DatabaseError
from connection_tools_v2.database import Database, DatabaseConnectionError


try:
    with Database() as connection:
        # Create a cursor object
        cursor = connection.cursor()

        # execute the SQL statement
        cursor.execute("""
            SELECT table_name
            FROM information_schema.tables
            WHERE table_schema = 'public'  -- Adjust schema if necessary
            AND table_type = 'BASE TABLE'
            ORDER BY table_name
        """)
        tables = cursor.fetchall()
        print(tables)

        if tables:
            print("Tables in the database:")
            for table in tables:
                print(table)
        else:
            print("No tables found in the database.")

        connection.commit()

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
