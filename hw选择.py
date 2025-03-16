def selectionSort(alist):
    for passnum in range(len(alist) - 1, 0, -1):
        max = 0
        for i in range(1, passnum + 1):
            if alist[i] > alist[max]:
                max = i
        alist[max], alist[passnum] = alist[passnum], alist[max]


s = ['P', 'Y', 'T', 'H', 'O', 'N']
selectionSort(s)
print(s)
