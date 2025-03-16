#print('hello world')
#将内容写到文件里去，注意file
#fp=open('E:/TEXT.txt','a+')#a+可以在每一次编译后为文本增加内容
#print('hello',file=fp)
#fp.close()

#转义字符\
print('hello\nworld')
print('hello\tworld')
print('helloooo\tworld')
print('hellooo\tworld')#四个为一个制表位
print('hello\rworld')#回一行重新开始
print('hello\bworld')#回一格
print('hello\\world')
print('hello\'hello\'')
print(r'hello\\\\world')#r使转义字符失效

#进制转换
print('二进制',0b11010100)#0b
print('八进制',0o74653)#0o
print('十六进制',0x34EA)#0x
#一些浮点数相加时，会出现一些精确度上的问题。
#这是因为计算机把他们转化为二进制运算，想要得到正确结果，可用如下一段代码
from decimal import Decimal
print(Decimal('1.1')+Decimal('2.2'))
#数据类型，布尔类型bool
f1=True
f2=False
print(f1,type(f1))
print(f1+1)
print(f2+1)
#字符串类型：不可变的字符序列。
#单双引号定义的字符串必须在同一行，三引号(单双都行）的可以连续多行
str1='''hello 
world'''
print(str1)
#数据类型转换：连接不同的数据类型
name='王小二'
age=13
print('他的名字是',name,'，今年',str(age),'岁')
print('他的名字是'+name+'，今年'+str(age)+'岁')
print(float(age))
#w2='hello'
#print((w2))
#将str类型转成int类型时，字符串必须为数字串且为整数
