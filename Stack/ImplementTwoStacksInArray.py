class TwoStack:
    def __init__(self, n):
        self.cap = n
        self.top1 = -1
        self.top2 = n
        self.arr = [0]*n

    def push1(self, x):
        if self.top1 < self.top2-1:
            self.top1 += 1
            self.arr[self.top1] = x
            return True
        else:
            return False

    def push2(self,x):
        if self.top1 < self.top2 - 1:
            self.top2 -= 1
            self.arr[self.top2] = x
            return True
        else:
            return False

    def pop1(self):
        if self.top1>=0:
            x = self.arr[self.top1]
            self.top1 -= 1
            return x
        else:
            return None

    def pop2(self):
        if self.top2 < self.cap:
            x = self.arr[self.top2]
            self.top2 += 1
            return x
        else:
            return None

    def size1(self):
        print(self.top1 + 1)

    def size2(self):
        print(self.cap - self.top2)

    def display(self):
        print(self.arr)


ts = TwoStack(10)
ts.push1(12)
ts.push2(21)
ts.push1(23)
ts.push1(34)
ts.push1(45)
ts.size1()
ts.size2()
ts.display()