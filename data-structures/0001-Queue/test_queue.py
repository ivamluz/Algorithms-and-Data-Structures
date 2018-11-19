import unittest
from queue import Queue

class TestQueue(unittest.TestCase):
  def test_peek_returns_none_when_queue_is_empty(self):
    q = Queue()
    self.assertIsNone(q.peek())

  def test_size_is_zero_when_queue_is_empty(self):
    q = Queue()
    self.assertEquals(q.size(), 0)

  def test_dequeue_returns_none_when_queue_is_empty(self):
    q = Queue()
    self.assertIsNone(q.dequeue())

  def test_size_is_greather_than_zero_when_queue_is_not_empty(self):
    q = Queue()
    q.enqueue(1)
    q.enqueue(3)
    q.enqueue(5)
    self.assertEquals(q.size(), 3)

  def test_peek_is_not_none_when_queue_is_not_empty(self):
    q = Queue()
    q.enqueue(3)
    self.assertEquals(q.peek(), 3)

  def test_dequeue_is_not_none_when_queue_is_not_empty(self):
    q = Queue()
    q.enqueue(1)
    self.assertEquals(q.dequeue(), 1)

  def test_queue_is_empty_after_last_item_is_dequeued(self):
    q = Queue()
    q.enqueue(1)
    q.dequeue()
    self.assertEquals(q.size(), 0)
    self.assertTrue(q.isEmpty())
    self.assertIsNone(q.peek())

  def test_item_is_enqueued(self):
    q = Queue()
    q.enqueue(1)
    self.assertEquals(q.peek(), 1)

    q.enqueue(3)
    self.assertEquals(q.peek(), 1)

    q.enqueue(5)
    self.assertEquals(q.peek(), 1)

    self.assertEquals(q.size(), 3)

  def test_lifo_order(self):
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)

    self.assertEquals(q.dequeue(), 1)
    self.assertEquals(q.dequeue(), 2)
    self.assertEquals(q.dequeue(), 3)

  def test_queue_works_after_getting_empty_and_item_is_enqueued(self):
    q = Queue()
    q.enqueue(1)
    q.dequeue()
    q.enqueue(3)
    q.enqueue(2)

    self.assertEquals(q.size(), 2)
    self.assertEquals(q.peek(), 3)

  def test_queue_is_empty(self):
    q = Queue()
    self.assertTrue(q.isEmpty())

  def test_queue_is_not_empty(self):
    q = Queue()
    q.enqueue(1)
    self.assertFalse(q.isEmpty())

if __name__ == '__main__':
  unittest.main()