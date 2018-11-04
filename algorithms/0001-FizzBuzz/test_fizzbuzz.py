import unittest
from fizzbuzz import fizzbuzz

class TestStringMethods(unittest.TestCase):

    def test_fizzbuzz(self):
        self.assertEqual(fizzbuzz(15), 'FizzBuzz')

    def test_fizz(self):
        self.assertEqual(fizzbuzz(3), 'Fizz')

    def test_buzz(self):
        self.assertEqual(fizzbuzz(5), 'Buzz')

    def test_not_matching(self):
        self.assertEqual(fizzbuzz(2), "2")

    def test_zero(self):
        self.assertIsNone(fizzbuzz(0))

    def test_negative_number(self):
        self.assertIsNone(fizzbuzz(-1))

if __name__ == '__main__':
    unittest.main()