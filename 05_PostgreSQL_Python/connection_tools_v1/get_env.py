import os
from dotenv import load_dotenv

load_dotenv()


def get_env():

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

    except ValueError as e:
        print(f"Environment variable error: {e}")

    env_var = (host, port, user, password, database)
    return env_var
