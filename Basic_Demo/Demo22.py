# if elif else结构



print('-------- case #1.取款 --------')
# money = 1000
# s = int(input('请输入取款金额: '))
#
# if money >= s:
#     money = money - s
#     print('取款成功，余额为: ', money)
# else:
#     print('取款不成功。')






print('-------- case #2.判断奇数还是偶数 --------')
# num = int(input('请输入一个整数: '))
#
# if num%2 == 0:
#     print(num, '是偶数')
# else:
#     print(num, '是奇数')






print('-------- case #3.判断输入成绩的范围 --------')
score = int(input('请输入一个成绩: '))

if 90 <= score <= 100: #score >= 90 and score <= 100:
    print('Grade A')
elif 80 <= score < 90: #score >= 80 and score < 90:
    print('Grade B')
elif 70 <= score < 80: #score >= 70 and score < 80:
    print('Grade C')
elif 60 <= score < 70: #score >= 60 and score < 70:
    print('Grade D')
elif 0 <= score < 60: #score >= 0 and score < 60:
    print('Grade E')
else:
    print('Sorry, please input a valid score (0 ~ 100).')

