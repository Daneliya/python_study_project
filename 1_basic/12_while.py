# while 基本格式
# while 条件A:
#     行动B
from unittest import removeResult

from setuptools.package_index import user_agent


# measure_brightness 函数返回当前测量的天空亮度
def measure_brightness():
    return 0


# 拍照片
def take_photo():
    pass


# for 循环写法
for i in range(100):
    # measure_brightness 函数返回当前测量的天空亮度
    if measure_brightness() >= 500:
        # 拍照片
        take_photo()

# while 改造后写法
# measure_brightness 函数返回当前测量的天空亮度
while measure_brightness() >= 500:
    # 拍照片
    take_photo()

# 使用while编写求平均值的计算器
print("哈喽呀！我是一个求平均值的程序。")
total = 0
count = 0
user_input = input("请输入数字（完成所有数字输入后，请输入q终止程序）：")
while user_input != "q":
    num = float(user_input)
    total += num
    count += 1
    user_input = input("请输入数字（完成所有数字输入后，请输入q终止程序）：")
if count == 0:
    result = 0
else:
    result = total / count
print("您输入的数字平均值为" + str(result))
