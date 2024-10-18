from unittest import TestCase
from linkedlist import LinkedList 

class LinkedListTest(TestCase):

    def test_addToHead(self):
        q = LinkedList()
        q.addToHead(5)
        q.addToHead(4)

        assert q.head.data == 4

    def test_addToTail(self):
        q = LinkedList()
        q.addToTail(45)
        q.addToTail(30)
        q.addToHead(400)

        assert q.tail.data == 30

    def test_addNode(self):
        q = LinkedList()
        q.addNode(5,0)
        q.addNode(4,0)

        assert q.head.next.data == 5

    def test_removeHead(self):
        q = LinkedList()
        q.addNode(5,0)
        q.addNode(4,1)
        q.removeHead()

        assert q.head.data == 4

