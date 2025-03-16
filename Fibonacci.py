def fibonacci(n):
    i=0
    a = 0
    b = 1
    for i in range(n):
        i=i+1
        c = a+b
        a = b
        b = c
    return c
def bn(x):
    ert = x**2 - 6*x + 2
    return ert
z = 2
p = 0
left = 0.00000
right = 10.00000
L1 = right - left
while z < 100:
    m = fibonacci(z)
    l = L1/m
    k = 1.000/m
    if k < 0.03:
        print("n=%s,Fn=%s"%(z,m))
        L2 = l*fibonacci(z-1)
        t = left + L2
        r = right -L2
        while p < 3:
            p = p + 1
            l3 = t - r
            e= bn(t)
            o = bn(r)
            if e>o :
                right = t
                t = r
                r = left + l3
            else:
                left = r
                r = t
                t = right - l3
        break
    else:
        z = z + 1

okk=(left+right)/2
okky=bn(okk)
print(left)
print(right)
print("极小值x=",okk)
print("极小值y=",okky)
