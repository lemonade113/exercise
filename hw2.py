name = input("请输入姓名；")
sum = 0
for i in range(3):
    grade = int(input("请输入第" + str(i + 1) + "门课的成绩："))
    sum += grade
ave = sum / (i + 1)
ave = ('%.2f' % ave)
print('Hello World ，Hello', name + '，Your average score is', str(ave))
