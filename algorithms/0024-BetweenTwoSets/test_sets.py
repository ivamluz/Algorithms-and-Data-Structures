import unittest
from sets import getTotalX


class TestGetTotalX(unittest.TestCase):
    def test_get_total_x(self):
        self.assertEquals(getTotalX([2, 4], [16, 32, 96]), 3)


if __name__ == "__main__":
    unittest.main()
