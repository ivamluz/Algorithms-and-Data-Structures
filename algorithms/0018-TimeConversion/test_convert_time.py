import unittest
from time_utils import convert_time


class TestConvertTime(unittest.TestCase):
    def testNoneValue(self):
        self.assertEquals(convert_time(None), "")

    def testEmptyValue(self):
        self.assertEquals(convert_time(""), "")

    def testAmTimeConversion(self):
        self.assertEquals(convert_time("07:05:45AM"), "07:05:45")

    def testPmTimeConversion(self):
        self.assertEquals(convert_time("07:05:45PM"), "19:05:45")

    def testMidnightTimeConversion(self):
        self.assertEquals(convert_time("12:30:10AM"), "00:30:10")

    def testNoonTimeConversion(self):
        self.assertEquals(convert_time("12:30:10PM"), "12:30:10")


if __name__ == "__main__":
    unittest.main()
