# sleep
from time import sleep
from datetime import datetime


# 输出当前时间
# print(now)

print(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

print("sleeping 5 seconds...")
sleep(5)

print(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
