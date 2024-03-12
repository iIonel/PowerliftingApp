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


def execute_query(query, values=None):
    """
    Executes a SQL query and returns the results as
    :param query:
    :param values:
    :return:
    """
    connection = connect_to_db()
    cursor = connection.cursor()

    if values is not None:
        cursor.execute(query, values)
    else:
        cursor.execute(query)

    connection.commit()
    final_result = cursor.fetchall()
    connection.close()
    return final_result
