from BinaryHeap import BinHeap

class PriorityQueue:
    def __init__(self):
        self.queue=BinHeap()

    def enqueue(self,item):
        self.queue.insert(item)
    def dequeue(self):
        self.queue.delMin()

