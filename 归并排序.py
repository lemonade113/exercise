def mergeSort(alist):
    if len(alist) <= 1:
        return alist
    middle = len(alist) // 2
    left = mergeSort(alist[:middle])
    right = mergeSort(alist[middle:])

    merged = []
    while left and right:
        if left[0] < right[0]:
            merged.append(left.pop(0))
        else:
            merged.append(right.pop(0))
    merged.extend(right if right else left)
    return merged


def merge_sort(alist):
    if len(alist) <= 1:
        return alist
    middle = len(alist) // 2
    left = merge_sort(alist[:middle])
    right = merge_sort(alist[middle:])

    i = 0
    j = 0
    k = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            alist[k] = left[i]
            i += 1
        else:
            alist[k] = right[j]
            j += 1
        k += 1
    while i < len(left):
        alist[k] = left[i]
        i += 1
        k += 1
    while j < len(right):
        alist[k] = right[j]
        j += 1
        k += 1

    print("Merging", alist)
