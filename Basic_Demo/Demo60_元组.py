# 元组




# t = ('hello','world',88,77,66) # 创建方式1
t = 'hello','world',88,77 # 创建方式2
# t = tuple(['hello','world',88]) # 创建方式3
print(id(t))
print(type(t))
print(t)


# 只有一种元素的情况下，必须加逗号，否则类型就是string
t1 = ('hello')
print(type(t1))
t2 = ('hello',)
print(type(t2))


# 空元组
# t3 = ()
t3 = tuple()
print(type(t3))