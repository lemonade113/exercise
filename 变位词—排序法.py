#先排序再比较O(nlogn)
def anagramSolution(s1,s2):
    alist1=list(s1)
    alist2=list(s2)
    alist1.sort()
    alist2.sort()
    pos=0
    stillOK=True
    while pos<len(s1) and stillOK:
        if alist1[pos]==alist2[pos]:
            #stillOK=True(多余）
            pos+=1
        else:
            stillOK=False
    return stillOK
print(anagramSolution('python','typhn'))
    
    