def toStr(n, base):
    print(1)
    convertString = '0123456789ABCDEF'
    if n < base:
        return convertString[n]
    else:
        return toStr(n // base, base) + convertString[n % base]



print(toStr(135, 3))
