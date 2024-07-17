import psycopg2
from psycopg2 import OperationalError, DatabaseError
from connection_tools_v2.config import load_config


class DatabaseConnectionError(Exception):
    pass


class Database:
    def __init__(self):
        self.config = load_config()
        self.connection = None

    def __enter__(self):
        try:
            self.connection = psycopg2.connect(**self.config)
            print(f'Connection established: {self.connection}')
            return self.connection
        except OperationalError as e:
            raise DatabaseConnectionError(
                f"Operational error while connecting to PostgreSQL: {e}")
        except DatabaseError as e:
            raise DatabaseConnectionError(f"Database error: {e}")

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.connection:
            self.connection.close()
            print("PostgreSQL connection is closed.")
