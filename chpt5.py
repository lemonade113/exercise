'''#字符串的驻留(pycharm进行了优化）
a=-100
b=-100
print(a is b)
c='123r'
d='123r'
print(a is b)
#字符串的查询
s='hello hello'
print(s.index('lo'))
print(s.find('lo'))
print(s.rindex('lo'))
print(s.rfind('lo'))

#字符串的大小写转换,转换后地址改变，因为字符串是不可变序列
p='hello world'
q=p.upper()
print(q)
print(p is q)
m=p.lower()
print(p==m)
print(p is m)#字符串一样但地址不同
s2='hEllo World'
print(s2.swapcase())#大写转小写，小写转大写
print(s2.capitalize())#把第一个字符转为大写，其它转换为小写
print(s2.title())#每个单词的首字母转为大写，其它转为小写

s='hello python'
#数字参数都是指定字符串宽度的，如果小于原字符串，则返回原字符串
print(s.center(20,'*'))#居中对齐，自定填充符
print(s.ljust(20,'*'))#左对齐
print(s.rjust(20,'*'))#右对齐
print(s.zfill(20))#用0填充，右对齐
print('-1089'.zfill(8))

#字符串的劈分
#从左边开始劈分，默认劈分符是空格，返回值为列表；sep指定劈分符；
#maxsplit最大劈分次数，剩余部分单独作为一部分
s='hello python world'
print(s.split())
s1='hello;python;world'
print(s1.split(sep=';'))
print(s1.split(sep=';',maxsplit=1))
print(s1.rsplit(sep=';',maxsplit=1))#从右分

#字符串的判断
print('1.','hello python world'.isidentifier())#判断是否是合法标识符
print('2.','_123_abc'.isidentifier())
print('3.','hellopythonworld'.isalpha())
print('4.','张三'.isalpha())#字母
print('5.','10101'.isdecimal())#十进制数
print('6.','一二34'.isdecimal())
print('7.','1254'.isnumeric())#数字
print('8.','一二34'.isnumeric())
print('9.','23432isdc'.isalnum())#数字和字母
print('10.','  \n'.isspace())#空白字符

#字符串替换
s='hello hello python'
print(s.replace('python','java'))
print(s.replace('hello','hi'))
print(s.replace('hello','hi',1))
#字符串合并
lst=['hello','python','what']
print('|'.join(lst))
print(' '.join(lst))
print('^'.join('python'))

#字符串的比较
print('apple'>'map')
print(ord('a'),ord('m'))
print(chr(99),chr(110))
print(ord('杨'))

#字符串的切片
s='today is a sunny day'
s1=s[11:]#没有end，默认到最后
s2=s[:5]#没有start，默认从开始
s3=s[2:13:2]#标准写法，[start:end:step]
newstr=s1+s2+s3
print(s1)
print(s2)
print(s3)
print(newstr)

#格式化字符串
name='lily'
age=34
#法一
print("我叫%s，今年%d岁"  %(name,age))
#法二
print("我叫{0}，今年{1}岁,真的叫{0}".format(name,age))#数字是索引
#法三
print(f"我叫{name}今年{age}岁")
print('%10d'  %99)
print('%.4f'  %3.1415926)
print('%10.4f'  %3.1415926)#同时设置宽度和精度
print('{0:.3}'.format(3.1415926))#.3表示一共三位数
print('{0:.3f}'.format(3.1415926))
'''
#字符串的编码转换
#将字符串转换为二进制数据（bytes）
s='举头望明月'
print(s.encode(encoding='GBK'))#在GBK这种编码中，一个中文字符占两个字节
print(s.encode(encoding='UTF-8'))#一个中文3个字节
byte=s.encode(encoding='GBK')
print(byte.decode(encoding='GBK'))#用GBK编，用GNK解
