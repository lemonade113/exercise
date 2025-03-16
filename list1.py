#列表的创建方式：使用中括号；调用内置函数list
lst=['hello',333,'world','hello']
'''lst2=list(['hello',333,'world'])
for item in lst:
    print(item,end='\t')
print(lst2)
print(lst[2])
'''
#列表的索引
#有重复的返回第一个;可在指定范围内查找
'''
print(lst.index('hello'))
print(lst.index('hello',1,4))
#获取特定索引的元素，还可以逆向（-n……-2，-1）
#列表元素的索引都是包含第一个，但不包含最后一个，如查找【1：3】就得到1，2，其它时候用到列表的索引同理
print(lst[2],lst[-3])
#获取列表多个元素[start,stop,step],得到新列表
lstt=lst[1:3:1]
print(lstt)
print('切片地址',id(lstt),'原地址',id(lst))
#步长为负,列表倒置
print(lst[3::-1])
#列表元素的判断及遍历
print('hello' in lst)
'''
#列表元素的增加
#append()在列表的末尾添加一个元素,添加之后还是同一个列表；extend（）在列表的末尾至少添加一个元素；
#insert（）在列表任意位置添加一个元素；切片在列表任意位置至少添加一个元素
'''lst.append(12)
print(lst)
lst1=['hello',333,'world','hello']
lst3=[22,'hh',77]
lst1.append(lst3)
print(lst1)
lst1=['hello',333,'world','hello']
lst1.extend(lst3)
print(lst1)
lst.insert(1,90)
print(lst)
lst[1:2]=lst3
print(lst)

#列表的删除
#remove删除一个指定的元素，重复只删第一个
#pop删除指定索引上的元素，不指定，则是删除最后一个
#切片
#clear清空列表
#del删除列表
lst5=[10,20,30,40]
#lst5.remove(20)
#lst5.pop(2)
#new_lst5=lst5[1:3]
#print(new_lst5)
lst5[1:3]=[]
print(lst5)
lst5.clear()
print(lst5)

#列表的排序
#sort改变原列表
lst6=[10,37,56,23,87]
lst6.sort()#默认升序
print(lst6)
lst6.sort(reverse=True)
print(lst6)
#sorted生成新列表
re_lst6=sorted(lst6,reverse=True)
print(re_lst6,id(lst6),id(re_lst6))
'''
#列表生成式,列表中的数有一定的规律
lst7=[i for i in range(9)]
print(lst7)
lst8=[i*i for i in range(9)]
print(lst8)
lst9=[i for i in range(0,11,2)]
print(lst9)



