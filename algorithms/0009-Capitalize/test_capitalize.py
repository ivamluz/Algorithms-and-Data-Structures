import unittest
from string_utils import capitalize

class TestCapitalize(unittest.TestCase):
  def test_none_array(self):
    self.assertEquals(capitalize(None), None)

if __name__ == '__main__':
  unittest.main()