

class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)
        print("After enqueue: ", self.items)

    def dequeue(self):
        print("Before dequeue: ", self.items)
        return self.items.pop()

    def size(self):
        return len(self.items)

    def print_queue(self):
        print("現在のキューの状態：", self.items)
        print()


a_queue = Queue()

for i in range(5):
    a_queue.enqueue(i)

print()

while a_queue.size():
    print("取り出した値：", a_queue.dequeue())
    a_queue.print_queue()

print()

a_queue.print_queue()

print("キューのサイズ：", a_queue.size())
