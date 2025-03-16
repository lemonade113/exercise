#输入函数input
#input输入默认为str类型
'''present=input('What do you want?')
print(present,type(present))'''
'''a=int(input('please input a number'))
b=int(input('please input another number'))
print(a+b,type(a+b))'''

#算数运算符
#除法运算/    整除运算//
'''print(11/2)
print(11//2)
#幂运算
print(2**10)
#除法向下取整
print(9//-4)
#取余遵循公式：余数=被除数-除数*商
#所以以下两个结果不同
print(9%-4)
print(-9%4)'''
#赋值运算符
#支持连等,实际上是一个整数，由三个引用指向，所以它们地址一样的
'''a=b=c=20;
print(a,id(a))
print(b,id(b))
print(c,id(c))
#参数赋值
a//=3
print(a)
#支持系列解包赋值,应用:交换数值
a,b,c=20,30,40
print(a,b,c)
a,b,c=c,b,a
print(a,b,c)'''

#比较运算符
#返回值类型为bool
'''a,b=10,10
print(a<b,type(a<b),int(a<b))
print(a is b)#用is比较变量的地址
list1=[11,22,33,44]
list2=[11,22,33,44]
print(list1==list2)
print(list1 is list2)
print(list1 is not list2)

#bool运算符
#not用于布尔运算值取反
ff1=True
ff2=False
print(not ff1)
s='helloworld'
print('k' in s)
print('h' in s)'''
#位运算符
a=37&22#&转为二进制后，比较对应每一位的数值，都是1则为1
d=37|22#对应位同为0则为0
b=bin(a).replace('0b','')
print(b)
c="{0:b}".format(a)
print(c)
print(4<<1)#向左移动一位，十进制*2
print(4>>1)#向右移动一位，十进制/2
