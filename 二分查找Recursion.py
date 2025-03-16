import numpy as np

'''
def binarySearch(alist, item):
    if len(alist) == 0:
        return False
    else:
        midpoint = len(alist) // 2
        if alist[midpoint] == item:
            return True
        else:
            if item < alist[midpoint]:
                return binarySearch(alist[:midpoint], item)
            else:
                return binarySearch(alist[(midpoint + 1):], item)
'''
def binarySearch(alist, item):
    if len(alist) == 1:
        if alist[0] == item:
            return True
        else:
            return False
    else:
        midpoint = len(alist) // 2
        if alist[midpoint] == item:
            return True
        else:
            if item < alist[midpoint]:
                return binarySearch(alist[:midpoint], item)
            else:
                return binarySearch(alist[(midpoint + 1):], item)



s = np.random.randint(100, size=20)
print("ori:", s)
print(binarySearch(s, 33))
