# 循环结构





print('-------- for循环 --------')
# for i in 'Python':
#     print(i)




print('-------- 输出1..10之间的整数 --------')
# for i in range(10):
#     print(i)



print('-------- 如果循环体不需要用到i变量，可自定义为“_” --------')
# for _ in range(5):
#     print('Python')






print('''-------- 输出100..999之间的水仙花数, 
         举例:
         153 = 3*3*3 + 5*5*5 + 1*1*1
--------''')
for i in range(100,1000):
    ge = i % 10 # 得到个位数
    shi = i // 10 % 10 # 得到十位数
    bai = i // 100 # 得到百位数
    # print(bai_wei_shu, shi_wei_shu, ge_wei_shu)

    if ge**3 + shi**3 + bai**3 == i:
        print(i)