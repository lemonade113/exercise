import timeit
import random
#快速排序
def quick_sort(lst):
    if len(lst) < 2:
        return lst
    mid = lst[len(lst)//2]
    left = list()
    right = list()
    lst.remove(mid)
    for i in lst:
        if i >= mid:
            right.append(i)
        else:
            left.append(i)
    #递归，不断地分，再排序
    new_lst = quick_sort(left)+[mid]+quick_sort(right)
    return new_lst

#控制列表个数
for n in range(10, 100, 10):
    test = timeit.Timer("quick_sort(s)", "from __main__ import quick_sort,s")
    s = list()
    #生成列表
    for length in range(n):
        i = random.randrange(100)
        s.append(i)
    s_new = quick_sort(s)
    time = test.timeit(number=1000)
    print(s_new,end='\t\t')
    print('%10.5f'%time)



