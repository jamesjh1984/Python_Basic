# 布尔运算符




print('-------- 布尔运算符 --------')



print('-------- in 和 not in --------')
s = 'HelloWorld'

print('W' in s)
print('w' in s)
print('k' in s)

print('W' not in s)
print('w' not in s)
print('k' not in s)

print('-------- 以下对象的布尔值为False --------')
print(bool(False))
print(bool(-1))
print(bool(-1.0))
print(bool(None))
print(bool(''))
print(bool(""))
print(bool([])) # 空列表
print(bool(list())) # 空列表
print(bool(())) # 空元组
print(bool(tuple())) # 空元组
print(bool({})) # 空字典
print(bool(dict())) # 空字典
print(bool(set()))# 空集合




print('-------- 其他对象的布尔值为True --------')
print(bool(17))
print(bool(True))
print(bool('HelloWorld'))
