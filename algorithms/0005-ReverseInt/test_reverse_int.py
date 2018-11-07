import unittest
from reverse_int import reverse_int

class TestReverseInt(unittest.TestCase):
  def test_zero(self):
    self.assertEqual(reverse_int(0), 0)

  def test_single_digit_number(self):
    self.assertEqual(reverse_int(1), 1)

  def test_multiple_digits_number(self):
    self.assertEqual(reverse_int(123), 321)

  def test_number_ending_with_zero(self):
    self.assertEqual(reverse_int(3200), 23)

  def test_negative_single_digit_number(self):
    self.assertEqual(reverse_int(-1), -1)

  def test_negative_multiple_digits_number(self):
    self.assertEqual(reverse_int(-23), -32)

  def test_negative_number_ending_with_zeros(self):
    self.assertEqual(reverse_int(-2300), -32)

  def test_none(self):
    self.assertEqual(reverse_int(None), None)

if __name__ == '__main__':
  unittest.main()