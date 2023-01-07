import unittest
from knapsack import unboundedKnapsack


class TestUnboundedKnapsack(unittest.TestCase):
    def test_matching_target_sum(self):
        self.assertEquals(unboundedKnapsack(12, [1, 6, 9]), 12)

    def test_not_matching_target_sum(self):
        self.assertEquals(unboundedKnapsack(10, [3, 8]), 9)


if __name__ == "__main__":
    unittest.main()
