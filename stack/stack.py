class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class Stack:
    def __init__(self):
        self.size = 0
        self.head = None

    def push(self, data):
        newNode = Node(data)

        if self.head:
            newNode.next = self.head

        self.head  = newNode
        self.size += 1
            

    def pop(self):
    
        if self.is_empty():
            return "The stack is empty"
        
        popped_node = self.head
        self.head = popped_node.next  
        self.size -= 1

        return popped_node.data
    
    def peek(self):

        if self.is_empty():
            return "The stack is empty"
        
        top_element = self.head.data

        return top_element
    
    def is_empty(self):
        return self.size == 0
    
    def stack_size(self):
        return self.size
    

stack = Stack()



        