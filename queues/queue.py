class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class Queue:

    def __init__(self):
        self.size = 0
        self.head = None
        self.tail = None

    def enqueue(self, element):
        newNode = Node(element)

        if self.head:
            self.tail.next = newNode
        else:
            self.head = newNode
            self.tail = newNode
        
        self.tail = newNode
        self.size += 1

    def dequeue(self):
        if not self.head:
            return "The queue is empty"
        
        popped_node = self.head
        self.head = self.head.next
        self.size -= 1

        if self.head == None:
            self.tail = None

        return popped_node.data
    
    def queue_size(self):
        return self.size
    
    def front(self):
        if self.isEmpty():
            return "The queue is empty"
        
        return self.head.data
    
    def isEmpty(self):

        return self.size == 0
    