import timeit
import random
'''
def del_dict(x):
    random_index = random.randrange(len(x) - 1)
    try:
        del x[random_index]
    except KeyError:
        x.setdefault(random_index, None)
        del x[random_index]

'''
def del_dict(x):
    key_try = random.randrange(len(x) - 1)
    while x.get(key_try) == None:
        key_try = random.randrange(len(x) - 1)
    del x[key_try]


print("i\t\tlist_del_time\t\tdict_del_time")
for i in range(10000, 100001, 10000):
    lst_time = timeit.Timer("index = random.randrange(len(x)-1);del x[index]", "from __main__ import random, x")
    dict_time = timeit.Timer("del_dict(x)", "from __main__ import random, x, del_dict")
    x = list(range(i))
    list_del_time = lst_time.timeit(number=2000)
    x = {j:True for j in range(i)}
    dict_del_time = dict_time.timeit(number=2000)
    print("%d %10.3f %20.3f" %(i, list_del_time, dict_del_time))

