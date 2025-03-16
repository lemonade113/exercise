from Stack_ori import Stack


def baseConverter(decNum, base):
    digits = '0123456789ABCDEF'
    s = Stack()
    while decNum > 0:
        rem = decNum % base
        s.push(rem)
        decNum = decNum // base
    new = ''
    while not s.isEmpty():
        new = new + digits[(s.pop())]
    return new


print(baseConverter(89708, 16))