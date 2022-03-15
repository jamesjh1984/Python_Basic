# 列表




list1 = ['hello','world',88,77,66]
list2 = list(['hello','world',88])
print(id(list1))
print(type(list1))
print(list1)
print(list1[0])
print(list1[1])
print(list1[2])

print(list1.index('hello'))
print(list1.index('world'))
print(list1.index(88))

# 在一个范围内查找
# print(list1.index(66,0,3))
print(list1.index(66,0,5))

# 判断在列表中是否存在
print(10 in list1)
print(88 in list1)
print(10 not in list1)
print(88 not in list1)



print('--------------------------------')


for i in list1:
    print(i)


print('--------------------------------')

