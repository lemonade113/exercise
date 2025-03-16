import numpy as np


def bubbleresort(alist):
    l = 0
    r = len(alist) - 1
    count = 0
    change = True
    while l < r and change:
        change = False
        for i in range(l, r):
            if alist[i] > alist[i + 1]:
                change = True
                alist[i], alist[i + 1] = alist[i + 1], alist[i]
        r -= 1
        for i in range(r, l, -1):
            if alist[i] < alist[i - 1]:
                change = True
                alist[i], alist[i - 1] = alist[i - 1], alist[i]
        l += 1

        count += 1

    print(count)


# s=np.random.randint(100,size=10)
s = [9, 2, 3, 4, 5, 6, 7, 8, 1]
bubbleresort(s)
print(s)
