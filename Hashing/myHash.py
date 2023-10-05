class MyHash:
    def __init__(self, b):
        self.cap = b
        self.size = 0
        self.arr = [-1 for i in range(self.cap)]

    def search(self, key):
        h = key % self.cap
        i = h
        while self.arr[i] != -1:
            if self.arr[i] == key:
                return True
            i = (i + 1) % self.cap
            if i == h:
                return False
        return False

    def insert(self, key):
        if self.size == self.cap:
            return False
        i = key % self.cap
        while self.arr[i] != -1 and self.arr[i] != -2 and self.arr[i] != key:
            i = (i + 1) % self.cap
        if self.arr[i] == key:
            return False
        else:
            self.arr[i] = key
            self.size += 1
            return True

    def erase(self, key):
        h = key % self.cap
        i = h
        while (self.arr[i] != -1):
            if self.arr[i] == key:
                self.arr[i] = -2
                return True
            i = (i + 1) % self.cap
            if i == h:
                return False
        return False

    def display(self):
        print(*self.arr)

h1 = MyHash(7)
h1.insert(70)
h1.insert(54)
h1.insert(61)
h1.insert(9)
h1.display()
print(h1.erase(54))
h1.display()

