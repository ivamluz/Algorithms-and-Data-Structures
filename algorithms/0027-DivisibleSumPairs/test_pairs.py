import unittest
from pairs import divisibleSumPairs


class TestDivisibleSumPairs(unittest.TestCase):
    def test_is_divisible(self):
        self.assertEquals(divisibleSumPairs([1, 3, 2, 6, 1, 2], 3), 5)

    def test_is_not_divisible(self):
        self.assertEquals(divisibleSumPairs([1, 3, 4], 6), 0)


if __name__ == "__main__":
    unittest.main()
