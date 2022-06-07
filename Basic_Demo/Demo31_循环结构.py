# 循环结构





print('-------- range函数 --------')
r = range(10) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(r)
print('r =', list(r))



r = range(1, 10) # [1, 2, 3, 4, 5, 6, 7, 8, 9]
print('r =', list(r))



x = range(1, 10, 2) # [1, 3, 5, 7, 9]
print('x =', list(x))

print('10 in x: ', 10 in x)
print('9 in x: ', 9 in x)

print('10 not in x: ', 10 not in x)
print('9 not in x: ', 9 not in x)