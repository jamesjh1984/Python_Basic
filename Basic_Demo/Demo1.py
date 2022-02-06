# print函数

# 输出到屏幕
print(520)
print(98.5)

print('Hello World')

print(3+1)



# 输出到文件
fp = open('./Demo1.txt', 'a+') # a+: 如果不存在就创建，若存在就在后面追加
print('Hello World 222', file=fp)
fp.close()




# 不换行输出
print('Hello', 'World', 'Python')