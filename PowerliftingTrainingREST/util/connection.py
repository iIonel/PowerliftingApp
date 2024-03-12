import psycopg2


def connect_to_db():
    """
    Trying connecting to the PostgreSQL database.
    """
    try:
        connection = psycopg2.connect(
            database="postgres",
            host="localhost",
            user="postgres",
            password="1234",
            port="5433"
        )
        return connection
    except psycopg2.Error as e:
        print("Error connecting to PostgreSQL database:", e)
        return None
