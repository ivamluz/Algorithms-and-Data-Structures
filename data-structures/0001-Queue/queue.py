class Queue:
  def __init__(self):
    self._size = 0
    self._tail = None
    self._head = None
    self._data = {}

  def peek(self):
    if self._data.has_key(self._head):
      return self._data[self._head]
    else:
      return None

  def size(self):
    return self._size

  def isEmpty(self):
    return self.size() == 0

  def enqueue(self, item):
    if self.isEmpty():
      self._data[0] = item
      self._head = 0
      self._tail = 0
    else:
      self._tail += 1
      self._data[self._tail] = item

    self._size += 1

  def dequeue(self):
    if not self._data.has_key(self._head):
      return None

    item = self._data[self._head]

    del self._data[self._head]

    if not self.isEmpty():
      self._head += 1
    else:
      self._head = None
      self._tail = None

    self._size -= 1
  
    return item