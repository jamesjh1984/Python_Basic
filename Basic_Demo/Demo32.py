# 循环结构





print('-------- while循环 --------')
# x = 1
# while x <= 10:
#     print(x)
#     x += 1



print('-------- 计算1..100之间的偶数和 --------')
x = 1
sum = 0
while x <= 100:
    if x % 2 == 0:
        sum += x
    x += 1
print('1..100之间的偶数和:', sum)