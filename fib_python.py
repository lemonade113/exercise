import timeit
import random


def fibonacci_re(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fibonacci_re(n-1) + fibonacci_re(n-2)


def fibonacci_cir(n):
    result = 0
    n1 = 1
    n2 = 1
    if n == 1 or n == 2:
        result = 1
    else:
        for i in range(n-2):
            result = n1 + n2
            n1 = n2
            n2 = result
    return result


n = random.randrange(1, 15)

re_test = timeit.Timer('fibonacci_re(%d)' % n,
                       'from __main__ import n,fibonacci_re')
cir_test = timeit.Timer('fibonacci_cir(%d)' % n,
                        'from __main__ import n,fibonacci_cir')

res1 = fibonacci_re(n)
res2 = fibonacci_cir(n)

time1 = re_test.timeit(2000)
time2 = cir_test.timeit(2000)

print('n =', n)
print('The re_result is %d, the time is %8.5f'%(res1, time1))
print('The cir_result is %d, the time is %8.5f'%(res2, time2))
#n=1-3的时候递归快，n大一些的时候循环明显快于递归