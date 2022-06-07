# 嵌套循环





print('-------- 输出一个三行四列的矩形 --------')
# for i in range(3): # 三行
#     for j in range(4): # 四列
#         print('*', end='\t') # 不换行输出
#     print() # 换行





print('-------- 输出一个九行的直角三角形 --------')
# for i in range(1, 10): # 三行
#     for j in range(1, i+1): # 四列
#         print('*', end='\t') # 不换行输出
#     print() # 换行






print('-------- 输出九九乘法表 --------')
for i in range(1, 10): # 三行
    for j in range(1, i+1): # 四列
        print(j,'*', i, '=', i*j, end='\t') # 不换行输出
    print() # 换行