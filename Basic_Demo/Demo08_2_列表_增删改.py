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


# 切片
list3=['a','b','c']
list1[1:] = list3
print(list1)



print('--------------------------------')


# 删除

list1 = [1,2,3,4,5,6,7,8,9]

# 根据元素内容删除
list1.remove(4)
print(list1)
# list1.remove(100)

# 根据索引移除
list1.pop(1)
print(list1)

# 不写索引，将删除最后一个元素
list1.pop()
print(list1)

# 切片
print(list1[1:4])

# 清空所有元素
list1.clear()
print(list1)

# 删除list1对象
# del list1
# print(list1)




print('--------------------------------')


# 修改

list5 = [1,2,3,4,5,6,7,8,9]
list5[2] = 22
print(list5)
list5[1:3] = [222,333,444]
print(list5)




print('--------------------------------')


# 排序

list6 = [55,88,33,11,77,99,66,44,22]
print(list6, id(list6))

# 升序
# list6.sort()
list6.sort(reverse=False)
print(list6, id(list6))

# 降序
list6.sort(reverse=True)
print(list6, id(list6))



print('')


# 使用sorted()内置函数排序，将产生一个新的列表对象
list7 = [55,88,33,11,77,99,66,44,22]
print(list7, id(list7))

# 升序
new_list7 = sorted(list7)
print(new_list7, id(new_list7))

# 降序
new_list7 = sorted(list7, reverse=True)
print(new_list7, id(new_list7))