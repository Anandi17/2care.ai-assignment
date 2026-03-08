import psycopg2

def get_connection():

    conn = psycopg2.connect(
        host="localhost",
        database="appointments",
        user="postgres",
        password="password"
    )

    return conn