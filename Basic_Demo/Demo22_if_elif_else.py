# if elif else结构



print('-------- 常规if else --------')
x = int(input('请输入一个整数 x: '))
y = int(input('请输入一个整数 y: '))

# if x >= y:
#     print(str(x) +' >= ' + str(y))
# else:
#     print(str(x) +' < ' + str(y))


print('-------- 使用if else条件表达式 --------')
print(str(x) +' >= ' + str(y) if x >= y else str(x) +' < ' + str(y))