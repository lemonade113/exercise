def facsum(num):
    sum=0
    for i in range(1,num+1):
        fac = 1
        for j in range(1,i+1):
            fac=j*fac
        sum=sum+fac
    return sum

n=int(input("请输入一个整数："))
print(facsum(n))




