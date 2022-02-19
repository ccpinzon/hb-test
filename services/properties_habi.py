import json


def get_habi_property_list(query_filters):
    if not query_filters or not query_filters.strip():
        print("Return all data empty")
        return None

    json_data = json.loads(query_filters)

    if json_data is None:
        print("Return all data")
        return None

    if 'filters' not in json_data or len(json_data['filters']) == 0:
        print("Return all data because not filters")
        return None

    filters = json_data['filters']

    if 'year' in filters:
        print("add year filter")

    if 'city' in filters:
        print("add city filter")

    if 'status' in filters:
        print("add status filter")

    print(f'FiltersJSON ==>> ', json_data)

    return None
