# 转义字符

# 换行
print('Hello\nWorld')

# 水平制表符
print('Hello\tWorld')

# 回车符
print('Hello\rWorld')

# 退格符(退一个格)
print('Hello\bWorld')


print('http:\\\\www.baidu.com')

print('Teacher says: \'Hello.\'')



# 原字符，不希望转义字符起作用
print(r'Hello\nWorld')
# 注意事项，最后一个字符不能是反斜杠，否则报错如下：
# print(r'Hello\nWorld\')
print(r'Hello\nWorld\\') # 最后两个\\可以