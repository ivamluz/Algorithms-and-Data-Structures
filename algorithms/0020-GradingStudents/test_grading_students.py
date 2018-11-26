import unittest
from grades import gradingStudents

class TestGradingStudents(unittest.TestCase):
    def test_rounds_if_difference_to_multiple_of_five_is_less_than_3(self):
        self.assertEquals(gradingStudents([73]), [75])

    def test_does_not_round_if_difference_to_multiple_of_five_is_not_less_than_3(self):
        self.assertEquals(gradingStudents([67]), [67])

    def test_rounds_if_grade_is_min_grade_and_difference_to_multiple_of_five_is_less_than_3(self):
        self.assertEquals(gradingStudents([38]), [40])

    def test_does_not_round_if_grade_is_less_than_min_min_grade(self):
        self.assertEquals(gradingStudents([33]), [33])

    def test_multiple_cases(self):
        self.assertEquals(gradingStudents([73, 67, 38, 33]), [75, 67, 40, 33])

if __name__ == '__main__':
    unittest.main()