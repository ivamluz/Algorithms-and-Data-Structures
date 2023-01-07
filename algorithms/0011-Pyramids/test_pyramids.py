import unittest
from pyramids import pyramids


class TestPyramids(unittest.TestCase):
    def test_negative_levels(self):
        with self.assertRaises(ValueError):
            self.assertRaises(pyramids(-1))

    def test_zero_levels(self):
        with self.assertRaises(ValueError):
            self.assertRaises(pyramids(0))

    def test_single_level(self):
        self.assertEquals(pyramids(1), "#")

    def test_double_level(self):
        expected_output = " # \n"
        expected_output += "###"

        self.assertEquals(pyramids(2), expected_output)

    def test_multiple_levels(self):
        expected_output = "    #    \n"
        expected_output += "   ###   \n"
        expected_output += "  #####  \n"
        expected_output += " ####### \n"
        expected_output += "#########"

        self.assertEquals(pyramids(5), expected_output)


if __name__ == "__main__":
    unittest.main()
