class UnorderedList:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head == None

    def add(self, item):
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp


lst = UnorderedList()
lst.add(45)
lst.add(57)
lst.add(88)
print(lst)