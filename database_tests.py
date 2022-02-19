import unittest
from database import connect_db as conn
from shared import constants as cons


class DBTesting(unittest.TestCase):

    def test_simple_query(self):
        data = conn.exec_query_sql("SELECT * FROM property")

        self.assertTrue(len(data) > 0)  # add assertion here

    def test_get_properties_db_without_filters(self):
        data = conn.exec_query_sql(cons.SQL_PROPERTIES_WITHOUT_FILTERS)
        self.assertTrue(len(data) > 0)


if __name__ == '__main__':
    unittest.main()
