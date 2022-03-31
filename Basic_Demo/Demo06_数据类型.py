# 数据类型



######## 1. 整数 ########
n1 = 90
n2 = -76
n3 = 0
print(n1, type(n1))
print(n2, type(n2))
print(n3, type(n3))

# 整数可以表示为二进制，十进制，八进制，十六进制
print('十进制: ', 327)
print('二进制 --> 十进制: ', 0b10101111)
print('八进制 --> 十进制: ', 0o176)
print('十六进制 --> 十进制: ', 0x1EAF)





######## 2. 浮点数 ########
a = 3.1415926
print(a, type(a))

a1 = 1.1
a2 = 2.2
a3 = 2.1

# 浮点数计算会出现不精确性
print(a1 + a2) # 3.3000000000000003
print(a1 + a3) # 3.2

# 可以引入模块解决浮点不精确性
from decimal import Decimal
print(Decimal('1.1') + Decimal('2.2'))





######## 3. 布尔类型 ########
b1 = True
b2 = False

print(b1, type(b1))
print(b2, type(b2))

# 布尔值可以转换成整数计算
print(b1 + 0)
print(b2 + 0)






######## 4. 字符串类型 ########
# 单引号，双引号只能显示一行
str1 = 'ABCD,EFG'
str2 = "ABCD,EFG"

# 三引号可以显示多行
str3 = """ABCD,
EFG"""
str4 = '''ABCD,
EFG'''

print(str1, type(str1))
print(str2, type(str2))
print(str3, type(str3))
print(str4, type(str4))






######## 5. 类型转换 ########
x1 = 18
x2 = '18'
x3 = 98.5
x4 = '82.6'
x5 = True
x6 = 'Hello'


print('-------- str() --------')
print(str(x1), type(str(x1)))


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