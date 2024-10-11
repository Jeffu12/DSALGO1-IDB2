class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)
        print(f"Enqueued {item}: {self.items}")

    def dequeue(self):
        if not self.is_empty():
            dequeued_item = self.items.pop(0)
            print(f"Dequeued {dequeued_item}: {self.items}")
            return dequeued_item
        print("Queue is empty!")
        return "Queue is empty!"

    def is_empty(self):
        return len(self.items) == 0

    def __len__(self):
        return len(self.items)


def first(Q):
    if not Q.is_empty():
        print(f"First item: {Q.items[0]}")
        return Q.items[0]
    print("Queue is empty!")
    return "Queue is empty!"

Q = Queue()
Q.enqueue(5)
Q.enqueue(3)
print(f"Len: {len(Q)}")
print(f"Dequeue: {Q.dequeue()}")
print(f"Is queue empty? {Q.is_empty()}")
print(f"Dequeue: {Q.dequeue()}")
print(f"Is queue empty? {Q.is_empty()}")
print(f"Dequeue: {Q.dequeue()}")
Q.enqueue(7)
Q.enqueue(9)
print(f"First item in the queue: {first(Q)}")
Q.enqueue(4)
print(f"Length of queue: {len(Q)}")
print(f"Dequeue: {Q.dequeue()}")
print(f"Queue is Q = {Q.items}")
print()

print("Second part")
R = Queue()
R.enqueue(5)
R.enqueue(3)
print(f"Dequeue: {R.dequeue()}")
R.enqueue(2)
R.enqueue(8)
print(f"Dequeue: {R.dequeue()}")
print(f"Dequeue: {R.dequeue()}")
R.enqueue(9)
R.enqueue(1)
print(f"Dequeue: {R.dequeue()}")
R.enqueue(7)
R.enqueue(6)
print(f"Dequeue: {R.dequeue()}")
print(f"Dequeue: {R.dequeue()}")
R.enqueue(4)
print(f"Dequeue: {R.dequeue()}")
print(f"Dequeue: {R.dequeue()}")
print(f"Queue is = {R.items}")
