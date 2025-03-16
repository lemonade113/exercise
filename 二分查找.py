


def binarySearch(alist, item):
    sum=0
    first = 0
    last = len(alist) - 1
    found = False
    while first <= last and not found:
        sum+=1
        midpoint = (first + last) // 2
        if alist[midpoint] == item:
            found = True

        elif alist[midpoint] < item:
            first = midpoint + 1

        else:
            last = midpoint - 1

    print(sum)
    return found


s = [1,4,6,11,19,35,52,54,57,71,78,86,92,96]
print(binarySearch(s, 21))

