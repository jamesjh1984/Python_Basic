# 元组




t = (10,[20,30],40)
print(t)
print(type(t))

print(t[0],type(t[0]),id(t[0]))
print(t[1],type(t[1]),id(t[1]))
print(t[2],type(t[2]),id(t[2]))

# 元组不允许修改元素
# t[1] = 100
# 可以向列中添加元素
t[1].append(100)
print(t)



# 元组遍历
for i in t:
    print(i)