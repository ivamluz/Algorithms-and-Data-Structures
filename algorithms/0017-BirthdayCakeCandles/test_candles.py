import unittest
from candles import birthdayCakeCandles

class TestBirthdayCakeCandles(unittest.TestCase):
    def test_none_values(self):
        self.assertEquals(birthdayCakeCandles(None), 0)

    def test_empty_values(self):
        self.assertEquals(birthdayCakeCandles([]), 0)

    def test_unsorted_values(self):
        self.assertEquals(birthdayCakeCandles([3, 2, 1, 3]), 2)

    def test_sorted_asc_values(self):
        self.assertEquals(birthdayCakeCandles([1, 2, 3, 3]), 2)

    def test_sorted_desc_values(self):
        self.assertEquals(birthdayCakeCandles([3, 3, 2, 1]), 2)

    def test_single_return_value(self):
        self.assertEquals(birthdayCakeCandles([3, 2, 1, 4]), 1)

    def test_single_input_value(self):
        self.assertEquals(birthdayCakeCandles([3]), 1)

if __name__ == '__main__':
    unittest.main()