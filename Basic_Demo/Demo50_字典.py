# 字典



# 创建
dict1 = {'A':21, 'B':22, 'C':23, 'D':24, 'E':25} # 创建方式1
print(dict1, id(dict1), type(dict1))

dict2 = dict(name='A', age=21) # 创建方式2
print(dict2, id(dict2))

dict3 = {}
print(dict3, id(dict3))




print('--------------------------------')

# 获取元素
print(dict1['A'])
# print(dict1['Z']) # 报错

print(dict1.get('B'))
print(dict1.get('Z')) # 不报错
print(dict1.get('Z',0)) # 不报错，找不到返回默认值0



print('--------------------------------')

print('A' in dict1)
print('A' not in dict1)




print('--------------------------------')

# return all keys
keys = dict1.keys()
print(keys, type(keys))

# 转换为List
print(list(keys))




# return all values
values = dict1.values()
print(values, type(values))

# 转换为List
print(list(values))






# return all key-value pairs
item_pairs = dict1.items()
print(item_pairs, type(item_pairs))

# 转换为List
print(list(item_pairs))



print('--------------------------------')


for i in dict1:
    print(i, dict1[i], dict1.get(i))
