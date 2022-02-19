SQL_PROPERTIES_WITHOUT_FILTERS = '''
SELECT
    p.id,p.address,p.city,s.name status,p.price, p.description
FROM status_history sh
INNER JOIN status s on sh.status_id = s.id
INNER JOIN property p on sh.property_id = p.id
WHERE sh.update_date = (
    SELECT MAX(update_date)
        FROM status_history sb
    WHERE sb.property_id=sh.property_id
    AND sb.status_id IN (3,4,5)  -- “pre_venta”, “en_venta” y “vendido”
)
'''

SQL_FILTER_YEAR = "\n AND p.year = '$_YEAR_$'"
SQL_FILTER_CITY = "\n AND p.city = '$_CITY_$'"
SQL_FILTER_STATUS = "\n AND s.name = '$_STATUS_NAME_$'"

SQL_ORDER_BY = '\n order by sh.property_id asc'
