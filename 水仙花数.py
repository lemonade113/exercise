def shuixian(n):
    if int(n) >= 100:
        sum = 0
        m = len(n)
        for item in n:
            i = int(item)
            sum = i ** m + sum
        return sum == int(n)
    else:
        return "输入值不合法！"


max = int(input("请输入一个大于等于1000的整数："))
if (max < 1000):
    print("输入值不合法！")
else:
    for i in range(100, max + 1):
        flag = shuixian(str(i))
        if (flag):
            print(i, end='\t')
