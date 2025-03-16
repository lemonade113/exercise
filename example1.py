#计算1到100的偶数和
sum=0;
for n in range(1,101):
    if n%2==0:
        sum+=n
print('和为：',sum)

nn=1
sum2=0
while nn<=100:
    if nn%2==0:
       sum2+=nn
    nn+=1
print('和为：',sum2)

#输入密码，三次后结束
'''
for n in range(3):
    password = input('请输入密码：')
    if password == '8888':
        print('输入正确')
        break
    else:
        if(n<2):
          print('输入错误，请第'+str(n+2)+'次输入')
if(n==2):
    print("不允许再输入")
'''

#输出1到50之间5的倍数
for n in range(1,11):
    if(n%5==0):
        print(n)
#反向思维：如果不是5的倍数就不输出
for n2 in range(1,11):
    if(n2%5!=0):
        continue
    print(n2)

