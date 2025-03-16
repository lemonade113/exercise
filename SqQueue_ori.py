class SqQueue:
    def __init__(self, maxsize):
        self.queue = [None] * maxsize
        self.maxsize = maxsize
        self.front = 0
        self.rear = 0

    def size(self):
        return (self.rear - self.front + self.maxsize) % self.maxsize

    #队尾rear加元素,时间复杂度为O(1)
    def EnQueue(self, data):
        if (self.rear + 1) % self.maxsize == self.front:#判断队满的条件
            print("The queue is full!")
        else:
            self.queue[self.rear] = data
            self.rear = (self.rear + 1) % self.maxsize

    #队首front删元素,时间复杂度为O(1)
    def DeQueue(self):
        if self.rear == self.front:
            print("The queue is empty!")
        else:
            data = self.queue[self.front]
            self.queue[self.front] = None
            self.front = (self.front + 1) % self.maxsize
            return data

    def Print(self):
        print(self.queue)


test = SqQueue(15)
for i in range(10):
    test.EnQueue(i)
test.Print()
test.DeQueue()
test.Print()
for i in range(3):
    test.EnQueue(i)
test.Print()
