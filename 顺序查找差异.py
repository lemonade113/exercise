import timeit
import random


def binarySearch(alist, item):
    first = 0
    last = len(alist) - 1
    found = False
    while first <= last and not found:
        midpoint = (first + last) // 2
        if alist[midpoint] == item:
            found = True
        elif alist[midpoint] < item:
            first = midpoint + 1
        else:
            last = midpoint - 1
    return found


def orderedSequentialSearch(alist, item):
    pos = 0
    found = False
    stop = False
    while pos < len(alist) and not found and not stop:
        if alist[pos] == item:
            found = True
        elif alist[pos] > item:
            stop = True
        else:
            pos += 1
    return found


print("i\t\t二分查找\t\t顺序查找")
for i in range(1000, 10001, 1000):
    bi_time = timeit.Timer("binarySearch(s, item)",
                           "from __main__ import binarySearch,s, item")
    or_time = timeit.Timer("orderedSequentialSearch(s,item)",
                           "from __main__ import orderedSequentialSearch,s,item")
    s = list(range(i))
    item = random.randrange(i)
    biSearchTime = bi_time.timeit(1000)
    orSearchTime = or_time.timeit(1000)
    print("%d %10.5f %10.5f" % (i, biSearchTime, orSearchTime))
