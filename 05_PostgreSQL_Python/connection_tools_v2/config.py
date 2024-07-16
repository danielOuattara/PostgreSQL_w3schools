import os
from dotenv import load_dotenv


def load_config():
    load_dotenv()  # Load environment variables from .env

    host = os.getenv("HOST")
    port = os.getenv("PORT")
    user = os.getenv("DB_USERNAME")
    password = os.getenv("DB_PASSWORD")
    database = os.getenv("DATABASE")

    if not all([host, port, user, password, database]):
        raise ValueError(
            "One or more environment variables are missing: HOST, PORT, DB_USERNAME, DB_PASSWORD, DATABASE")

    return {
        "host": host,
        "port": port,
        "user": user,
        "password": password,
        "database": database,
    }
