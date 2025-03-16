import numpy as np


def shellSort(alist):
    sublistcount = len(alist) // 2
    while sublistcount > 0:
        for startposition in range(sublistcount):
            gapInsertSort(alist, startposition, sublistcount)
        print("After increments of size", sublistcount,
              "The list is", alist)
        sublistcount = sublistcount // 2


def gapInsertSort(alist, startposition, gap):
    for i in range(startposition + gap, len(alist), gap):
        currentValue = alist[i]
        position = i - gap
        while position >= 0 and alist[position] > currentValue:
            alist[position + gap] = alist[position]
            position -= gap
        alist[position + gap] = currentValue


s = np.random.randint(100, size=10)
print("ori:", s)
shellSort(s)
