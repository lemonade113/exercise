from 无序表链表 import UnorderedList
import timeit
import random
def remove_linked(x, num):
    item = random.randrange(num)
    try:
        x.remove(item)
    except KeyError:
        item = random.randrange(num)
        x.remove(item)

for i in range(10000, 100000, 10000):
    linked_Remove = timeit.Timer('remove_linked(linkedList, %d)'% i,
                             'from __main__ import linkedList,remove_linked')
    python_Remove = timeit.Timer('pythonList.pop(random.randrange(%d))' % i,
                              'from __main__ import pythonList')
    linkedList = UnorderedList()
    for j in range(i):
        linkedList.add(j)
    pythonList = list(range(i))
    linked_RemoveTime = linked_Remove.timeit(100)
    python_RemoveTime = python_Remove.timeit(100)
    print('%d, %10.3f, %10.3f' % (i, linked_RemoveTime, python_RemoveTime))
