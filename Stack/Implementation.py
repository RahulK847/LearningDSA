class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []
    def push(self, data):
        self.items.append(data)

    def pop(self):
        if not self.is_empty():
            popped_element = self.items.pop()
            print("Popped: ",popped_element )
        else:
            print("No Element available to pop.")
    def peek(self):
        if not self.is_empty():
            print("Peek Element is: ", self.items[-1])
        else:
            print("NONE")
    def size(self):
        print(len(self.items))


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