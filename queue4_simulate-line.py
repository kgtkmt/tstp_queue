

import time
import random

class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)
        # print("After enqueue: ", self.items)

    def dequeue(self):
        # print("Before dequeue: ", self.items)
        return self.items.pop()

    def size(self):
        return len(self.items)

    def print_queue(self):
        print("現在のキューの状態：", self.items)
        print()

# till_show : あと何秒で映画が始まるか
# max_time  : ある人がチケットを買うのにかかる最大の秒数
def simulate_line(till_show, max_time):
    pq = Queue()
    tix_sold = []  # チケットを購入できた人のリスト

    for i in range(100):
        pq.enqueue("person" + str(i))

    print()

    t_end = time.time() + till_show
    now = time.time()

    while now < t_end and not pq.is_empty():
        now = time.time()
        r = random.randint(0, max_time)
        time.sleep(r)
        person = pq.dequeue()
        print(person)
        tix_sold.append(person)
    return tix_sold

sold = simulate_line(5, 1)
print()
print(sold)
