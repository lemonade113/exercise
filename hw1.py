'''lst=['a','b','c','d']
for i in lst:
    print(i)
'''
stuIm = [
    {'name': '小李', 'age': 19, 'address': '上海宝山'},
    {'name': '小王', 'age': 18, 'address': '江苏南京'},
    {'name': '小张', 'age': 19, 'address': '山东济南'}
]
print(stuIm)

'''
telNum=["18621320022","110000123a"]
for s in telNum:
    print('请输入电话号码：',s)
    if len(s)==11 and s.isdigit():
        print('是合法电话号码')
    else:
        print('不是合法电话号码')

name=input("请输入姓名；")
sum=0
for i in range(3):
   grade=int(input("请输入第"+str(i+1)+"门课的成绩："))
   sum+=grade
ave=sum/(i+1)
print('Hello World ，Hello',name+'，Your average score is',str(ave))
'''
