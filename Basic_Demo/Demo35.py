# continue语句




print('-------- 要求输出1..50之间所有5的倍数，例如：5,10,15 --------')
# for i in range(1, 51):
#     if i % 5 == 0:
#         print(i)


for i in range(1, 51):
    if i % 5 != 0:
        continue
    print(i)