from Node import Node
import random
class UnorderedList:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head == None

    def add(self, item):
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp

    def length(self):
        current = self.head
        count = 0
        while current != None:
            count = count + 1
            current = current.getNext()
        return count

    def search(self, item):
        current = self.head
        found = False
        while current != None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()
        return found

    def remove(self, item):
        current = self.head
        previous = None
        found = False
        while current != None and not Found:
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()
        if previous == None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())

    '''
    def remove2(self):
        current = self.head
        previous = None
        while current != None:
            previous = current
            current = current.getNext()
        previous = None
    '''
    def slice(self, start, stop):
        current = self.head
        num = 1
        slice_lst = list()
        while num < start:
            current = current.getNext()
            num += 1
        for i in range(start, stop):
            slice_lst.append(current.getData())
            current = current.getNext()
        return slice_lst


lst = UnorderedList()
for i in range(20):
    lst.add(i)
new_lst = lst.slice(5,11)
print(new_lst)




