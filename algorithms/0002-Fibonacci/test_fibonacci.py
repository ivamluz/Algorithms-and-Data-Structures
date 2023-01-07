import unittest
from fibonacci import build_fibonacci_sequence_up_to


class TestFibonacci(unittest.TestCase):
    def test_negative_number(self):
        self.assertEqual(build_fibonacci_sequence_up_to(-1), None)

    def test_zero(self):
        self.assertEqual(build_fibonacci_sequence_up_to(0), None)

    def test_single_sequence(self):
        self.assertEqual(build_fibonacci_sequence_up_to(1), [0, 1, 1])

    def test_small_max_value(self):
        self.assertEqual(build_fibonacci_sequence_up_to(5), [0, 1, 1, 2, 3, 5])

    def test_larger_max_value(self):
        self.assertEqual(
            build_fibonacci_sequence_up_to(100),
            [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89],
        )


if __name__ == "__main__":
    unittest.main()
