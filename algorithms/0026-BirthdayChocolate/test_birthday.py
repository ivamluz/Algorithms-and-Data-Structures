import unittest
from birthday import birthday

class TestBirthday(unittest.TestCase):
    def test_no_square(self):
        self.assertEquals(birthday(numbers = [1, 1, 1, 1, 1, 1], day = 3, month = 2), 0)

    def test_single_square(self):
        self.assertEquals(birthday(numbers = [4], day = 4, month = 1), 1)

    def test_multiple_squares(self):
        self.assertEquals(birthday(numbers = [1, 2, 1, 3, 2], day = 3, month = 2), 2)

if __name__ == '__main__':
    unittest.main()