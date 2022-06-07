# @Coding: utf-8
# @Time: 2022/5/12 22:43
# @Author: James Jin
# @Project: Python_Basic
# @File: Demo15_逻辑运算符


# and
print('-------- and --------')
print('True and True =>', True and True)
print('True and False =>', True and False)
print('False and True =>', False and True)
print('False and False =>', False and False)


# or
print('-------- or --------')
print('True or True =>', True or True)
print('True or False =>', True or False)
print('False or True =>', False or True)
print('False or False =>', False or False)


# not 取反
print('-------- not --------')
print('not True =>', not True)
print('not False =>', not False)




# 逻辑运算符性能提升
print('-------- 逻辑运算符性能提升 --------')

a = 36

# a > 10 and print('Hello A')
# a < 10 and print('Hello B') # 只要前面是False，后面就不执行

a > 10 or print('Hello A') # 只要前面是True，后面就不执行
a < 10 or print('Hello B')