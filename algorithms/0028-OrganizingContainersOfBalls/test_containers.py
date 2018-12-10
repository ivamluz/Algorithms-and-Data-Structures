import unittest
from containers import organizingContainers, RESULT_IMPOSSIBLE, RESULT_POSSIBLE

class TestOrganizingContainers(unittest.TestCase):
    def test_impossible(self):
        containers = [
            [1, 3, 1],
            [2, 1, 2],
            [3, 3, 3]
        ]
        self.assertEquals(organizingContainers(containers), RESULT_IMPOSSIBLE)

    def test_possible(self):
        containers = [
            [0, 2, 1],
            [1, 1, 1],
            [2, 0, 0]
        ]
        self.assertEquals(organizingContainers(containers), RESULT_POSSIBLE)

if __name__ == '__main__':
    unittest.main()