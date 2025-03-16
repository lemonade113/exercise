a = float(input("请输入一个十进制数："))
ls_in = list()
ls_de = list()
a_in = int(a)
a_de = a - a_in
# 整数部分
while a_in >= 1:
    b = a_in % 2
    a_in = a_in // 2
    ls_in.append(b)
ls_in.reverse()
# 小数部分
for i in range(8):
    if a_de == 0:
        break
    a_de = a_de * 2
    if (a_de >= 1):
        ls_de.append(1)
        a_de = a_de - 1
    else:
        ls_de.append(0)
        a_de = a_de
# 将列表转化为数字形式输出
for i in ls_in:
    print(i, end='')
if (ls_de != []):
    print('.', end='')
for j in ls_de:
    print(j, end='')
