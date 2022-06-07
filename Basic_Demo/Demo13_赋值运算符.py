# 赋值运算符


a = b = c = 20
print(a, id(a))
print(b, id(b))
print(c, id(c))



a = 20
a += 30
print('a = 20,a += 30', a)

a -= 10
print('a -= 10',a)

a *= 2
print('a *= 2', a)

a /= 3
print('a /= 3', a)

a //= 2
print('a //= 2', a)




print('-------- 解包赋值 --------')
a, b ,c = 20, 30, 40
print(a, b, c)




print('-------- 交换两个变量的值 --------')
a, b = 10, 20
print('Before: ', a, b)

a, b = b, a
print('After: ', a, b)