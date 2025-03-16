def insertSort(alist):
    for current in range(1, len(alist)):
        currentValue = alist[current]
        position = current - 1
        while currentValue < alist[position] and position >= 0:
            alist[position + 1] = alist[position]
            position -= 1
        alist[position + 1] = currentValue