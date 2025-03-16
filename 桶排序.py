import random
DEFAULT_BUCKET_SIZE = 5
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

def bucket_sort(data_list,bucket_size = DEFAULT_BUCKET_SIZE):
    length = len(data_list)
    min = max = data_list[0]
    #寻找最小值和最大值
    for i in range(0,length):
        if data_list[i] < min:
            min = data_list[i]
        if data_list[i] > max:
            max = data_list[i]
    #定义多个桶并初始化
    num_of_buckets = (max - min) // bucket_size +1
    buckets = []
    for i in range(num_of_buckets):
        buckets.append([])
    #将数据放入桶中
    for i in range(0,length):
        buckets[(data_list[i] - min)//bucket_size ].append(data_list[i])
    #依次对桶内数据进行快速排序
    data_list.clear()
    for i in range(num_of_buckets):
        print(f"第{i}个桶排序前的内容是{buckets[i]}")
        quick_sort(buckets[i])
        # print(f"第{i}个桶排序后的内容是{buckets[i]}")
    for data in buckets[i]:
        data_list.append(data)


data_list = [random.randint(0,15) for _ in range(0,15)]
print(data_list)
bucket_sort(data_list)
print(data_list)