import unittest
from array_utils import chunk

class TestArrayChunk(unittest.TestCase):
  def test_none_array(self):
    self.assertEquals(chunk(None, 1), [])

  def test_empty_array(self):
    self.assertEquals(chunk([], 1), [])

  def test_single_element_array(self):
    self.assertEquals(chunk([1], 1), [[1]])

  def test_split_to_single_sized_chunks(self):
    self.assertEquals(chunk([1, 2, 3], 1), [[1], [2], [3]])

  def test_equal_sized_chunks(self):
    self.assertEquals(chunk([1, 2, 3, 4], 2), [[1, 2], [3, 4]])

  def test_smaller_last_chunk(self):
    self.assertEquals(chunk([1, 2, 3, 4, 5], 2), [[1, 2], [3, 4], [5]])

  def test_size_greather_than_input(self):
    self.assertEquals(chunk([1, 2, 3], 4), [[1, 2, 3]])

  def test_invalidates_negative_size(self):
    with self.assertRaises(ValueError):
      self.assertRaises(chunk([1, 2, 3], -1))

  def test_invalidates_zeroed_size(self):
    with self.assertRaises(ValueError):
      self.assertRaises(chunk([1, 2, 3], 0))
    

if __name__ == '__main__':
  unittest.main()