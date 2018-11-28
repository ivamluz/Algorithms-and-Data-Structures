import unittest
from fruits import countApplesAndOranges

class TestCountApplesAndOranges(unittest.TestCase):
    def testNoApplesButOranges(self):
        result = countApplesAndOranges(
            house_start = 7,
            house_end = 10,
            apples_tree_location = 4,
            oranges_tree_location = 12 ,
            apple_distances = [1, 2, -4],
            orange_distances = [3, -1, -4]
        )

        self.assertEquals(result, (0, 1))

    def testNoOrangesButApples(self):
        result = countApplesAndOranges(
            house_start = 7,
            house_end = 10,
            apples_tree_location = 4,
            oranges_tree_location = 12 ,
            apple_distances = [1, 3, -4],
            orange_distances = [3, -1, 4]
        )

        self.assertEquals(result, (1, 0))

    def testNoApplesNorOranges(self):
        result = countApplesAndOranges(
            house_start = 7,
            house_end = 10,
            apples_tree_location = 4,
            oranges_tree_location = 12 ,
            apple_distances = [1, 2, -4],
            orange_distances = [3, -1, 4]
        )

        self.assertEquals(result, (0, 0))

    def testApplesAndOranges(self):
        result = countApplesAndOranges(
            house_start = 7,
            house_end = 10,
            apples_tree_location = 4,
            oranges_tree_location = 12 ,
            apple_distances = [2, 3, -4],
            orange_distances = [3, -2, -4]
        )

        self.assertEquals(result, (1, 2))

if __name__ == '__main__':
    unittest.main()