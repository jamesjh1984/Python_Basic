# 比较运算符


a = b = c = 20
print(a, id(a))
print(b, id(b))
print(c, id(c))



a = 20
a += 30
print(a)

a -= 10
print(a)

a *= 2
print(a)

a /= 3
print(a)

a //= 2
print(a)




print('-------- 解包赋值 --------')
a, b ,c = 20, 30, 40
print(a, b, c)




print('-------- 交换两个变量的值 --------')
a, b = 10, 20
print('Before: ', a, b)

a, b = b, a
print('After: ', a, b)