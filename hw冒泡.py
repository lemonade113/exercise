def shortBubbleSort(alist):
    change = True
    count=0
    passnum = len(alist) - 1
    while passnum > 0 and change:
        change = False
        for i in range(passnum):
            if alist[i] > alist[i + 1]:
                alist[i], alist[i + 1] = alist[i + 1], alist[i]
                change = True
        passnum -= 1
        count+=1
    print(count)


#s = ['P', 'Y', 'T', 'H', 'O', 'N']
s = [9, 2, 3, 4, 5, 6, 7, 8, 1]
shortBubbleSort(s)
print(s)
