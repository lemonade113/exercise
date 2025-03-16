def back(s, n):
    s1 = s[:-n]
    s2 = s[-n:]
    new_s = s2 + s1
    return new_s


s = input("请输入一个字符串：")
n = int(input("请输入向后循环移位的位数："))
print(back(s, n))
