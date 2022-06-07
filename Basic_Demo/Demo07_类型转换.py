# @Coding: utf-8
# @Time: 2022/5/12 21:47
# @Author: James Jin
# @Project: Python_Basic
# @File: Demo07_类型转换






######## 类型转换 ########
x1 = 18
x2 = '18'
x3 = 98.5
x4 = '82.6'
x5 = True
x6 = 'Hello'


print('-------- str() --------')
print(str(x1), type(str(x1)))
print(str(x3), type(str(x3)))
print(str(x5), type(str(x5)))



print('-------- int() --------')
print(int(x2), type(int(x2)))
print(int(x3), type(int(x3))) # 舍掉小数部分
# print(int(x4), type(int(x4))) # Error, 字符串不能为小数，需要为整数
print(int(x5), type(int(x5)))
# print(int(x6), type(int(x6))) # Error, 字符串需要为整数


print('-------- float() --------')
print(float(x4), type(float(x4)))
print(float(x2), type(float(x2)))
print(float(x5), type(float(x5)))
# print(float(x6), type(float(x6))) # Error, 字符串需要为数字
print(float(x1), type(float(x1)))




print('-------- bool() --------')
# 非0的整数(正负)都是True
# x1 = 18
# x1 = -18
# x1 = 0

# 有内容的字符串都是True
# x1 = 'AAAAAA'
# x1 = ''
# x1 = ""

# 有内容的列表都是True
# x1 = ['hello','world',88,77,66]
# x1 = []

# 有内容的元组都是True
# x1 = ('hello', 'world', 88, 77, 66)
# x1 = ()

# 有内容的元组都是True
# x1 = {'A':21, 'B':22, 'C':23, 'D':24}
x1 = {}

print(bool(x1), type(bool(x1)))