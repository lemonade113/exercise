def binarySearch(alist, item):
    first = 0
    last = len(alist) - 1
    while first < last:
        midpoint = (first + last) // 2
        if alist[midpoint] == item:
            return midpoint
        elif alist[midpoint] < item:
            first = midpoint + 1
        else:
            last = midpoint - 1
    return first+1