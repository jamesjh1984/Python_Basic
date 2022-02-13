# else语句





print('-------- 从键盘录入密码，最多三次，如果正确就结束循环 --------')
correct_pwd = '8888'
for i in range(3):
    pwd = input('请输入密码：')
    if pwd == correct_pwd:
        print('密码正确.')
        break
    else:
        print('密码不正确.')
else:
    print('对不起，三次密码均错误.')