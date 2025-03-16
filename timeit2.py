import timeit
import random
for i in range(10000, 100001, 10000):
    #random.randrange ([start,] stop [,step])
    dict_test = timeit.Timer('key = random.randrange(%d); x[key]=None' % i,
                             'from __main__ import x, random')
    x = {x: True for x in range(i)}
    dict_time = dict_test.timeit()
    print('%d, %10.3f' % (i, dict_time))
