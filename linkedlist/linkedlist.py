class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def addToHead(self, data):
        node = Node(data)

        if self.head:
            node.next = self.head
        else:
            self.head = self.tail = node
        
        self.head = node

    def removeHead(self):
        if not self.head:
            self.head = None
            self.tail = None
            return
        
        self.head = self.head.next

    def removeNode(self, data):

        current, previous, counter = self.head, None, 0

        while current:
            counter += 1
            if current.data == data:
                previous.next = current.next
            previous = current
            current  = current.next

        

    def addToTail(self, data):
        node = Node(data)

        if self.tail:
            self.tail.next = node
        else:
            self.head = self.tail = node

        self.tail = node

    def addNode(self, data, index):

        if index == 0:
            self.addToHead(data)
            return
        
        counter, current, previous, node = 0, self.head, None, Node(data)

        while current and counter < index:
            counter += 1
            previous = current
            current  = current.next

        node.next = current
        previous.next = node

    def print(self):

        current = self.head

        while current:
            print(current.data, end=" ")
            current = current.next
        print()
