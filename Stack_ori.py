#尾端作为栈顶
class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):       #时间复杂度为O(1)
        self.items.append(item)

    def pop(self):              #时间复杂度为O(1)
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)
#首段作为栈顶,不推荐
'''
class Stack_2:
    def __init__(self):
        self.items = []
        
    def isEmpty(self):
        return self.items == []
    
    def push(self, item):#时间复杂度为O(n)
        self.items.insert(0, item)
        
    def pop(self):#时间复杂度为O(n)
        return self.items.pop(0)
    
    def peek(self):
        return self.items[0]
    
    def size(self):
        return len(self.items)
'''