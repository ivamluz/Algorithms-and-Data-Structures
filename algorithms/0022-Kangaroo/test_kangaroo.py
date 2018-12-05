import unittest
from kangaroo import kangaroo, KANGAROO_RESULT_NO, KANGAROO_RESULT_YES

class TestKangaroo(unittest.TestCase):
    def test_positive_case(self):
        self.assertEquals(kangaroo(x1 = 0, v1 = 3, x2 = 4, v2 = 2), KANGAROO_RESULT_YES)

    def test_negative_case_when_resulting_steps_is_negative(self):
        self.assertEquals(kangaroo(x1 = 0, v1 = 2, x2 = 5, v2 = 3), KANGAROO_RESULT_NO)

    def test_negative_case_when_resulting_steps_is_positive_float(self):
        self.assertEquals(kangaroo(x1 = 21, v1 = 6, x2 = 47, v2 = 3), KANGAROO_RESULT_NO)

if __name__ == '__main__':
    unittest.main()