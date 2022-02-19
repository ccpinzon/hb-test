# from getpass import getpass
from mysql.connector import connect, Error


def conn_db():
    try:
        db_connection = connect(
            host="",
            port="3309",
            user="pruebas",
            passwd="",
            database="habi_db"
        )
        print(f"DATABASE ===> ", db_connection)
        return db_connection
    except Error as e:
        print(e)


def exec_query_sql(sql):
    if sql is None or sql.strip() == '':
        return None

    print(f"EXEC SQL ===>>> ", sql)
    db_conn = conn_db()
    cursor = db_conn.cursor()

    cursor.execute(sql)

    data = cursor.fetchall()

    return data

