'''
a=10
b=20
print(str(a)+'大于等于'+str(b)if a>=b else str(a)+'小于'+str(b))
r1=range(9)
print(list(r1))
r2=range(3,6)
print(list(r2))
r3=range(3,11,2)
print(list(r3))

for item in "python":
    print(item)
for num in r1:
    print(num)
'''
for i in range(1,10):
    for j in range(1,i+1):
        print(j,'*',i,'=',i*j,end='\t')#不换行输出
    print()

