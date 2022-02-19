# from getpass import getpass
import json

from mysql.connector import connect, Error


def conn_db():
    try:
        db_connection = connect(

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
    # column_names = json.loads(json.dumps(cursor.column_names))
    # print(f' columns -> ', column_names)

    data = cursor.fetchall()

    json_data = json.loads(json.dumps(data))
    list_data = []
    obj_data = {}

    for obj in json_data:
        # obj_data.update(id=obj[0])
        obj_data.update(address=obj[1])
        obj_data.update(city=obj[2])
        obj_data.update(status=obj[3])
        obj_data.update(price=obj[4])
        obj_data.update(description=obj[5])
        list_data.append(obj_data)
        obj_data = {}

    result = {}
    result.update(data=list_data)
    return result
