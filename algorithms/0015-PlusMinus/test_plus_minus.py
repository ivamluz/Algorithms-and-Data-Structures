import unittest
from matrix import plus_minus


class TestPlusMinus(unittest.TestCase):
    def test_none_value(self):
        self.assertEquals(plus_minus(None), [0, 0, 0])

    def test_empty_array(self):
        self.assertEquals(plus_minus([]), [0, 0, 0])

    def test_desc_sorted_array(self):
        self.assertEquals(plus_minus([1, 1, 0, -1, -1]), [0.400000, 0.400000, 0.200000])

    def test_asc_sorted_array(self):
        self.assertEquals(plus_minus([-1, -1, 0, 1, 1]), [0.400000, 0.400000, 0.200000])

    def test_unsorted_array(self):
        self.assertEquals(
            plus_minus([-4, 3, -9, 0, 4, 1]), [0.500000, 0.333333, 0.166667]
        )


if __name__ == "__main__":
    unittest.main()
