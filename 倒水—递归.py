from Stack_ori import Stack


def pour(c1, c2, g, x1, x2, buffer={}, path=[]):
    key = (x1, x2)
    if x1 == g or x2 == g :  # 递归边界：两个杯子各自等于需要的刻度数
        path.append(key)
        return True

    if key in buffer:  # 定义缓冲，判断是否已经递归过
        return buffer[key]


    buffer[key] = False

    if x1 > 0 and pour(c1, c2, g, 0, x2, buffer, path):  # 情况1：将x1倒空 (x1 > 0)
        path.append(key)
        buffer[key] = True
        return True

    if x2 > 0 and pour(c1, c2, g, x1, 0, buffer, path):  # 情况2： 将x2倒空 (x2 > 0)
        path.append(key)
        buffer[key] = True
        return True

    if x1 < c1 and pour(c1, c2, g, c1, x2, buffer, path):  # 情况3: 将x1倒满 (x1 < c1)
        path.append(key)
        buffer[key] = True
        return True

    if x2 < c2 and pour(c1, c2, g, x1, c2, buffer, path):  # 情况4：将x2倒满 (x2 < c2)
        path.append(key)
        buffer[key] = True
        return True

    if x1 + x2 < c2:
        if pour(c1, c2, g, 0, x1 + x2, buffer, path):  # 情况5：将x1倒入x2中，x1中无剩余
            path.append(key)
            buffer[key] = True
            return True
    else:
        if pour(c1, c2, g, x1 + x2 - c2, c2, buffer, path):  # 情况6：将x1倒入x2中，x1中有剩余
            path.append(key)
            buffer[key] = True
            return True

    if x1 + x2 < c1:  # 情况7：将x2导入x1中
        if pour(c1, c2, g, x1 + x2, 0, buffer, path):  # 情况7：将x2倒入x1中，x2中无剩余
            path.append(key)
            buffer[key] = True
            return True
    else:
        if pour(c1, c2, g, c1, x1 + x2 - c1, buffer, path):  # 情况8：将x2倒入x1中,x2中有剩余
            path.append(key)
            buffer[key] = True
            return True

    buffer[key] = False
    return False  # 不满足以上8种情况，则不能倒入


path = []
result = pour(5, 3, 4, 0, 0, path=path)
if result:
    for p in reversed(path):
        print(p)
else:
    print("No solution")



