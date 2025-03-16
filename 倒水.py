from Stack_ori import Stack


def pourwater(bottle1, bottle2, a, b, target):
    aEmpty = a
    n = 0
    while aEmpty >= 0:
        for i in range(b):
            bottle2.push('0')
        print(bottle1.size(), bottle2.size())
        for i in range(aEmpty):
            bottle1.push(bottle2.pop())
        print(bottle1.size(), bottle2.size())
        if bottle2.size() != target:
            while not bottle1.isEmpty():
                bottle1.pop()
            print(bottle1.size(), bottle2.size())
            while not bottle2.isEmpty():
                bottle1.push(bottle2.pop())
            print(bottle1.size(), bottle2.size())

            n += 1
            aEmpty = a - n * (b - a)

        else:
            break
    return 1


bottle1 = Stack()
bottle2 = Stack()
pourwater(bottle1, bottle2, 4, 5, 3)


