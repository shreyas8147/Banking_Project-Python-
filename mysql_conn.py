import mysql.connector


def connect_mysql(username, password, host="localhost", db=None):
    conn = mysql.connector.connect(
        host=host,
        user=username,
        password=password,
        database=db
    )


    return conn


def connect():
    conn = connect_mysql(
        username="root",
        password="Shreyas@7026",
        db="Banking"
    )
    return conn
