import unittest
from digits import findDigits

class TestFindDigits(unittest.TestCase):
    def test_all_are_divisors(self):
        self.assertEquals(findDigits(12), 2)

    def test_not_all_are_divisors(self):
        self.assertEquals(findDigits(1012), 3)

if __name__ == '__main__':
    unittest.main()