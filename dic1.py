# 字典，键值对。初始化字典的元素位置与实际位置无关（哈希函数）
# 键不允许重复，是不可变的对象
# 字典元素无序，没法指定位置插入
# 创建字典
scores = {'zhangsan': 100, 'lisi': 50, 'wamgwu': 98}
print(scores)
student = dict(name='zhangsan', age=30)
print(student)
# 获取字典的元素
print(scores['zhangsan'])
print(scores.get('zhangsan'))
# 如果查找的元素不存在，两者出现区别
# print(scores['www'])#会报错
print(scores.get('www'))
print(scores.get('www', 90))  # get可返回默认值
# 增删改
print('zhangsan' in scores)
del scores['zhangsan']
print(scores)
# scores.clear()
scores['chenliu'] = 88
print(scores)
scores['chenliu'] = 66
print(scores)

# 字典视图
kk = scores.keys()
print(kk)
print(type(kk))
print(list(kk))

vv = scores.values()
print(vv)
print(type(vv))
print(list(vv))

ii = scores.items()
print(ii)
print(list(ii))

# 字典元素的遍历
for i in scores:
    print(i, scores[i], scores.get(i))

items = ['aa', 'bb', 'cc']
prices = [34, 45, 56]
dict = {item.upper(): price for item, price in zip(items, prices)}
print(dict)

