from setuptools import setup, find_packages

setup(
    name='postgresql-connection',
    version='1.0',
    packages=find_packages(),
    install_requires=[
        'psycopg2',
        'python-dotenv',
    ],
)
