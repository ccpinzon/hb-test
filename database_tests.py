import unittest
from database import connect_db as conn


class DBTesting(unittest.TestCase):

    def test_simple_query(self):
        data = conn.exec_query_sql("SELECT * FROM property")

        self.assertTrue(len(data) > 0)  # add assertion here


if __name__ == '__main__':
    unittest.main()
