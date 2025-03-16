'''
#def 函数名（【输入参数】）
#    函数体
#    return
def calc(a,b):
    c=a+b
    return c
#位置实参
result=calc(10,20)
print(result)

#关键字实参（与c不同）
res=calc(b=10,a=20)#这里确实把10传给了形参b
print(result)
#在函数的调用过程中，如果是d不可变对象，函数内部的修改不会影响实参的值
#如果是可变对象，会改变
def test(arg1,arg2):
    print('arg1',arg1)
    print('arg2',arg2)
    arg1=100
    arg2.append(10)
    print('arg1_', arg1)
    print('arg2_', arg2)

n1=11
n2=[11,22,33]
print('n1', n1)
print('n2', n2)
test(n1,n2)
print('n1', n1)
print('n2', n2)

#返回值为多个，则返回元组
#形参可以带默认值参数

#可变的位置参数,实参个数可变，只能定义一个，结果为一个元组
def fun(*args):
    print(args)
fun(10)
fun(20,90)
#个数可变的关键字形参,只能定义一个，结果为一个字典
def func(**arges):
    print(arges)
func(a=10)
func(a=10,b=20,c=80)
#既有个数可变的关键字参数，又有个数可变的位置形参，要求位置形参放前面


def tion(a,b,c):
    print(a)
    print(b)
    print(c)
lst=[10,29,89]
dic={'a':100,'b':200,'c':300}
tion(*lst)
tion(**dic)
def tionn(a,b,*,c,d)#cd只能用关键字参数传递
    print(a,b,c,d)
#全局变量 global

def fac(n):
    if n==1:
        return 1
    else:
        return n*fac(n-1)
print(fac(6))

def fib(n):
    if n==1:
        return 1
    elif n==2:
        return 1
    else:
        return fib(n-1)+fib(n-2)
print(fib(4))
'''
print(ord('z'),ord('Z'))
print('a'<'z')