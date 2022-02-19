import json
from database import connect_db as conn
from shared import constants


def get_habi_property_list(query_filters):
    if not query_filters:
        return _get_habi_list_property()

    json_data = query_filters

    if json_data is None:
        return _get_habi_list_property()

    if 'filters' not in json_data or len(json_data['filters']) == 0:
        return _get_habi_list_property()

    filters = json_data['filters']

    return _get_habi_list_property(filters)


def sql_with_filters(sql, filters):
    if filters is None:
        return sql

    if 'city' in filters:
        sql = sql + constants.SQL_FILTER_CITY.replace('$_CITY_$', str(filters['city']))
    if 'year' in filters:
        sql = sql + constants.SQL_FILTER_YEAR.replace('$_YEAR_$', str(filters['year']))
    if 'status' in filters:
        sql = sql + constants.SQL_FILTER_STATUS.replace('$_STATUS_NAME_$', str(filters['status']))

    return sql


def _get_habi_list_property(filters=None):
    sql = constants.SQL_PROPERTIES_WITHOUT_FILTERS
    sql = sql_with_filters(sql, filters)
    sql = sql + constants.SQL_ORDER_BY

    try:
        data = conn.exec_query_sql(sql)
        return data
    except Exception as e:
        print(f"Error get data", e)
        return None


def _get_all_property_data():
    try:
        sql = constants.SQL_PROPERTIES_WITHOUT_FILTERS
        data = conn.exec_query_sql(sql)
        return data
    except Exception as e:
        print(f"Error get data", e)
        return None
