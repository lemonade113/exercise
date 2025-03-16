tr = [None, {'w': 2, 'v': 3}, {'w': 3, 'v': 4}, {'w': 4, 'v': 8},
      {'w': 5, 'v': 8}, {'w': 9, 'v': 10}]  # none占个位置
max_w = 20
m = {(i, w): 0 for i in range(len(tr))
     for w in range(max_w + 1)}
# 初始化二维表格m[(i,w)]
# 表示前i个宝物中，最大中w的组合所得的最大价值
for i in range(1, len(tr)):
    for w in range(max_w + 1):
        if tr[i]['w'] > w:  # 装不下第i个宝物
            m[(i, w)] = m[(i - 1, w)]  # 不装第i个宝物
        else:
            m[(i, w)] = max(m[(i - 1, w)], m[(i - 1, w - tr[i]['w'])] + tr[i]['v'])
print(m[len(tr) - 1, max_w])
