#O(n),但牺牲了空间,c1,c2需要的空间多
def anagramSolution(s1,s2):
    c1=[0]*26
    c2=[0]*26
    for item in s1:
        pos=ord(item)-ord('a')#取字母下标的技巧
        c1[pos]+=1
    for item in s2:
        pos=ord(item)-ord('a')
        c2[pos]+=1
    return c1==c2
print(anagramSolution('ab','ac'))      
    
        