from unittest import TestCase
from queue import Queue

class TestStack(TestCase):
    def test_push(self):
        pq = Queue()
        pq.enqueue(5)
        pq.enqueue(4)

        assert pq.front() == 5

    def test_pop(self):
        pq = Queue()
        pq.enqueue(5)
        pq.enqueue(4)
        pq.enqueue(3)
        assert pq.dequeue() == 5

    def test_peek(self):
        pq = Queue()
        pq.enqueue(5)
        pq.enqueue(4)

        assert pq.front() == 5

    def test_isEmpty(self):
        pq = Queue()
        pq.enqueue(5)
        pq.enqueue(4)
        pq.front()
        pq.dequeue()
        pq.dequeue()

        assert pq.isEmpty() == True

    def test_stack_size(self):
        pq = Queue()
        pq.enqueue(5)
        pq.enqueue(5)
        pq.enqueue(3)

        assert pq.queue_size() == 3