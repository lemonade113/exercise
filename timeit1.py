import timeit
import random
for i in range(10000, 100001, 10000):
    index_test = timeit.Timer('index = random.randrange(%d); x[index]' % i,
                              'from __main__ import x, random')
    x = list(range(i))
    index_time = index_test.timeit()
    print('%d, %10.3f' % (i, index_time))
