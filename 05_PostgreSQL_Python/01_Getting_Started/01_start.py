import psycopg2
from psycopg2 import OperationalError, DatabaseError
from dotenv import load_dotenv
import os

load_dotenv()  # Take environment variables from .env

try:

    # Get environment variables
    host = os.getenv("HOST")
    port = os.getenv("PORT")
    user = os.getenv("DB_USERNAME")
    password = os.getenv("DB_PASSWORD")
    database = os.getenv("DATABASE")

    if not all([host, user, password]):
        raise ValueError(
            "One or more environment variables are missing: HOST, DB_USERNAME, DB_PASSWORD")

    # Establish the connection
    connection = psycopg2.connect(
        host=host,
        port=port,
        user=user,
        password=password,
        database=database,
    )

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

except ValueError as e:
    print(f"Environment variable error: {e}")

finally:
    # Close the cursor and connection if they were established
    if 'cursor' in locals() and not cursor.closed:
        cursor.close()
        print("Cursor closed.")
    if 'connection' in locals() and connection and not connection.closed:
        connection.close()
        print("PostgreSQL connection is closed.")
