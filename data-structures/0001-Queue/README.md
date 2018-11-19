# Queue

Create a queue data structure. The queue should be a class with methods ```enqueue()```, ```dequeue()```, ```peek()``` and ```size```.

Enqueueing ane element should store an element until it is dequeued.

## Examples
```python
q = Queue()

q.enqueue(1)
q.enqueue(3)
q.enqueue(5)

q.size() # returns 3

q.peek() # returns 5

q.dequeue(); # returns 5 and remove it out of the queue;
```