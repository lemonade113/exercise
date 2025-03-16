#排序算法的优化：O(n)
import timeit
import random
def counting_sort(a):
    length = len(a)
    min = max = 0
    for i in range(0, length):
        if a[i] < min:
            min = a[i]
        if a[i] > max:
            max = a[i]
    counter = [0 for i in range(max - min + 1)]  # 用于统计个数的空数组
    for i in range(length):
        counter[a[i]-min] += 1  # 统计每个元素出现的次数
    n = 0
    for j in range(len(counter)):
        while counter[j] > 0:
            a[n] = j + min  # 取出元素
            n += 1
            counter[j] -= 1
    return a

'''
def new_sort(a):
    lst = [None]*100
    for i in a:
        j = i
        while(lst[j] != None):
            j += 1
        lst[j] = i
    res = list(filter(None, lst))
    return res

s=[10]*90
print(new_sort(s))
'''


'''
import random

lstData = random.sample(range(1,1000),10)
k = int(input("enter the value of kth element to find:"))

minData=min(lstData)
maxData=max(lstData)

ch = [0 for lstData in range(minData,maxData+1)]

for item in lstData:
    pos = item - minData
    ch[pos] = ch[pos] + 1
    
sum=0
pos = 0
while sum<k:
    sum = ch[pos] + sum
    pos = pos +1

x= pos-1 + minData
print("%d is the K'th element of the list" % (x))

'''


for n in range(10, 100, 10):
    test = timeit.Timer("counting_sort(s)", "from __main__ import counting_sort,s")
    s = list()
    #生成列表
    for length in range(n):
        i = random.randrange(100)
        s.append(i)
    s_new = counting_sort(s)
    time = test.timeit(number=1000)
    print(s_new,end='\t\t')
    print('%10.5f'%time)






