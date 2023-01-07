import unittest
from matrix import diagonal_difference


class TestDiagonalDifference(unittest.TestCase):
    def test_none_value(self):
        self.assertEquals(diagonal_difference(None), 0)

    def test_empty_matrix(self):
        self.assertEquals(diagonal_difference([]), 0)

    def test_odd_sized_matrix(self):
        input = [[11, 2, 4], [4, 5, 6], [10, 8, -12]]
        self.assertEquals(diagonal_difference(input), 15)

    def test_even_sized_matrix(self):
        input = [[11, 2, 4, -5], [4, 5, 6, 0], [10, 8, -12, 7], [7, 13, -8, 9]]
        self.assertEquals(diagonal_difference(input), 3)


if __name__ == "__main__":
    unittest.main()
