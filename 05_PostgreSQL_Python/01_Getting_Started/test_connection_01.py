"""
In this module:

- get the environment var
- establish the connection
- create the cursor
- close the connection

All in one module
"""


import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()  # Take environment variables from .env

# Get environment variables
host = os.getenv("HOST")
port = os.getenv("PORT")
user = os.getenv("DB_USERNAME")
password = os.getenv("DB_PASSWORD")
database = os.getenv("DATABASE")

print(f"Host: {host}")
print(f"Port: {port}")
print(f"User: {user}")
# Do not print password in production code
print(f"Password: {password}")

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
