def turn_num(s):
    lst1=s.split()
    lst2=list()
    num={'zero':'0','one':'1','two':'2','three':'3','four':'4','five':'5','six':'6','seven':'7','eight':'8','nine':'9'}
    for i in lst1:
        lst2.append(num[i])
    print(''.join(lst2))

s=input("请输入英文数字：")
turn_num(s)
