"""tool created by me, using a logical purpose"""


import psycopg2
from psycopg2 import OperationalError, DatabaseError
from connection_tools_v1.get_env import get_env


def connecting():
    try:

        env_var = get_env()

        # Establish the connection
        connection = psycopg2.connect(
            host=env_var[0],
            port=env_var[1],
            user=env_var[2],
            password=env_var[3],
            database=env_var[4],
        )

        print(f'Connection established: {connection}')

        return connection

    except OperationalError as e:
        print(f"Operational error while connecting to PostgreSQL: {e}")

    except DatabaseError as e:
        print(f"Database error: {e}")
