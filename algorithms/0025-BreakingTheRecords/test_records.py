import unittest
from records import breakingRecords


class TestBreakingRecords(unittest.TestCase):
    def test_breaking_both_records(self):
        self.assertEquals(breakingRecords([10, 5, 20, 20, 4, 5, 2, 25, 1]), (2, 4))

    def test_breaking_only_highest_score(self):
        self.assertEquals(
            breakingRecords([3, 4, 21, 36, 10, 28, 35, 5, 24, 42]), (4, 0)
        )

    def test_breaking_only_lowest_score(self):
        self.assertEquals(breakingRecords([3, 3, 3, 2, 1]), (0, 2))

    def test_never_breaking_either_score(self):
        self.assertEquals(breakingRecords([3, 3, 3, 3, 3]), (0, 0))


if __name__ == "__main__":
    unittest.main()
