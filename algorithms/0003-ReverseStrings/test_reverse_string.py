import unittest
from reverse_string import reverse


class TestReverseString(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(reverse(""), "")

    def test_none(self):
        self.assertEqual(reverse(None), None)

    def test_single_char(self):
        self.assertEqual(reverse("a"), "a")

    def test_small_string(self):
        self.assertEqual(reverse("abc"), "cba")

    def test_larger_string(self):
        self.assertEqual(
            reverse("A man, a plan, a canal: Panama"), "amanaP :lanac a ,nalp a ,nam A"
        )


if __name__ == "__main__":
    unittest.main()
