class Myhash:
    def __init__(self, bucket):
        self.bucket = bucket
        self.table = [[] for i in range(self.bucket)]

    def insect(self, key):
        i = key % self.bucket
        self.table[i].append(key)
    def remove(self, key):
        i = key % self.bucket
        self.table[i].remove(key)
    def display(self):
        print(self.table)

h1 = Myhash(7)
h1.insect(70)
h1.insect(56)
h1.insect(71)
h1.insect(9)
h1.insect(72)
h1.display()
h1.remove(9)
h1.display()
