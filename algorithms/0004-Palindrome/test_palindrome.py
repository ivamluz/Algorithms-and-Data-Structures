import unittest
from palindrome import is_palindrome


class TestIsPalindrome(unittest.TestCase):
    def test_phrase_with_spaces(self):
        self.assertTrue(is_palindrome("A man, a plan, a canal: Panama"))

    def test_none(self):
        self.assertFalse(is_palindrome(None))

    def test_empty_string(self):
        self.assertTrue(is_palindrome(""))

    def test_palindrome_with_even_length(self):
        self.assertTrue(is_palindrome("abba"))

    def test_non_palindrome_with_even_length(self):
        self.assertFalse(is_palindrome("abbc"))

    def test_palindrome_with_odd_length(self):
        self.assertTrue(is_palindrome("abCbA"))

    def test_non_palindrome_with_odd_length(self):
        self.assertFalse(is_palindrome("abcbC"))


if __name__ == "__main__":
    unittest.main()
