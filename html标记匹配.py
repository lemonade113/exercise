from Stack_ori import Stack
from Deque_ori import Deque


def HTalistMatch(s):
    s = s.split()
    element = ''
    temp = ''
    deq = Deque()
    stack = Stack()
    left = 0
    right = 0
    for i in s:
        flag = False
        for j in i:
            if j == '<':
                flag = True
                left += 1
                continue
            elif j == '>':
                flag = False
                element += ' '
                right += 1
            if flag:
                element += j

        temp = element.split()
        for str in temp:
            deq.addFront(str)

        element = ''

    Match = True
    if left != right:
        Match = False

    stack.push(deq.removeRear())
    while not deq.isEmpty() and Match:
        a = '/' + stack.peek()
        b = deq.removeRear()

        if a != b:
            stack.push(b)
        else:
            stack.pop()
    if not stack.isEmpty():
        Match = False

    return Match


print(HTalistMatch("<htalist> <title> E </title> </htalist>"))


