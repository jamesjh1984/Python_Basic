# 字典生成式



# 个数匹配
keys1 = ['A','B','C','D']
values1 = [21,22,23,24]

dict1 = {k:v for k,v in zip(keys1, values1)}
print(dict1)


print('--------------------------------')

# 个数不匹配
keys1 = ['A','B','C','D']
values1 = [21,22,23,24,25,26]

dict1 = {k:v for k,v in zip(keys1, values1)}
print(dict1)