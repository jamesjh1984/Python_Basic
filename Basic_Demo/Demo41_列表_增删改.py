# 列表



# 增加

list1 = ['hello','world',88,77,66]
print('before add: ', list1,id(list1))
list1.append(100)
print('after add: ', list1,id(list1))



list2=[11,22]
list1.append(list2)
print(list1)

list1.extend(list2)
print(list1)

list1.insert(1,'this')
print(list1)



list3=['a','b','c']
list1[1:] = list3
print(list1)



print('--------------------------------')


# 删除

list1 = [1,2,3,4,5,6,7,8,9]

list1.remove(4)
print(list1)
# list1.remove(100)

list1.pop(1)
print(list1)
