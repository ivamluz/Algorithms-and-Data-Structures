import unittest
from char_utils import most_occurring_chars


class TestMostOccurringChars(unittest.TestCase):
    def test_none_string(self):
        self.assertIsNone(most_occurring_chars(None))

    def test_empty_string(self):
        self.assertIsNone(most_occurring_chars(""))

    def test_string_with_spaces_only(self):
        self.assertEquals(most_occurring_chars("   "), {" ": 3})

    def test_single_most_occurring_char(self):
        self.assertEquals(most_occurring_chars("tutorial horizon"), {"o": 3})

    def test_multiple_most_occurring_chars(self):
        self.assertEquals(most_occurring_chars("abcabcdefabcab"), {"a": 4, "b": 4})


if __name__ == "__main__":
    unittest.main()
