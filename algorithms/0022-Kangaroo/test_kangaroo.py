import unittest
from kangaroo import kangaroo, KANGOROO_RESULT_NO, KANGOROO_RESULT_YES

class TestKangaroo(unittest.TestCase):
    def test_positive_case(self):
        self.assertEquals(kangaroo(x1 = 0, v1 = 3, x2 = 4, v2 = 2), KANGOROO_RESULT_YES)

    def test_negative_case(self):
        self.assertEquals(kangaroo(x1 = 0, v1 = 2, x2 = 5, v2 = 3), KANGOROO_RESULT_NO)

if __name__ == '__main__':
    unittest.main()