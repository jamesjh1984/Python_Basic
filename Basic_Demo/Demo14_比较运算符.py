# 比较运算符




print('-------- 比较运算符 --------')
a, b = 20, 30
print('a>b?', a>b)
print('a<b?', a<b)
print('a>=b?', a>=b)
print('a<=b?', a<=b)
print('a==b?', a==b)
print('a!=b?', a!=b)



print('-------- 标识比较运算符 数字 --------')
a = 10
b = 10
print('a==b?', a==b) # value相等
print('a is b?', a is b) # id标识(内存地址)相等
print('a is not b?', a is not b) # id标识(内存地址)相等
print('id(a): ', id(a))
print('id(b): ', id(b))




print('-------- 标识比较运算符 数组 --------')
list1 = [1,2,3,4]
list2 = [1,2,3,4]
print('list1==list2?', list1==list2) # value相等
print('list1 is list2?', list1 is list2) # id标识(内存地址)不相等
print('list1 is not list2?', list1 is not list2) # id标识(内存地址)不相等
print('id(list1): ', id(list1))
print('id(list2): ', id(list2))