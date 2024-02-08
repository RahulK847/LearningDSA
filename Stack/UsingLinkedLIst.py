class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:

    def __init__(self):
        self.head = None
        self.count = 0

    def is_empty(self):
        return self.head is None
    def push(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        self.count += 1

    def pop(self):
        if not self.is_empty():
            print("Popped: ", self.head.data)
            self.head = self.head.next
            self.count -= 1
        else:
            print("No available to pop.")

    def peek(self):
        if not self.is_empty():
            print("Peek element: ", self.head.data)
        else:
            print("NONE")

    def size(self):
        print(self.count)



s = Stack()

s.peek()
s.pop()
s.push(1)
s.size()
s.pop()
s.push(2)
s.peek()
s.push(3)
s.peek()
s.size()