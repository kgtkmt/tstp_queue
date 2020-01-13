

class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        print("Before dequeue: ", self.items)
        return self.items.pop()

    def size(self):
        return len(self.items)

    def print_queue(self):
        print("現在のキューの状態：", print(self.items))


a_queue = Queue()
print(a_queue.is_empty())
