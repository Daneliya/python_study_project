# 定义一个函数，计算扇形的面积
def calculate_sector(central_angle, radius):
    # 接下来是一些定义函数的代码
    sector_area = central_angle / 360 * 3.14 * radius ** 2
    print(f"此扇形面积为：{sector_area}")
    return sector_area


# 调用函数
sector_area_1 = calculate_sector(160, 30)
sector_area_2 = calculate_sector(60, 15)
sector_area_3 = calculate_sector(30, 16)

"""
写一个计算BMI的函数，函数名为 calculate_BMI。
1. 可以计算任意体重和身高的BMI值
2. 执行过程中打印一句话，“您的BMI分类为：xx”
3. 返回计算出的BMI值

BMI = 体重 / (身高 ** 2)

BMI分类
偏瘦: BMI <= 18.5
正常: 18.5 < BMI <= 25
偏胖: 25 < BMI <= 30
肥胖: BMI > 30
"""


def calculate_BMI(weight, height):
    BMI = weight / height ** 2
    if BMI <= 18.5:
        category = "偏瘦"
    elif 18.5 < BMI <= 25:
        category = "正常"
    elif 25 < BMI <= 30:
        category = "偏胖"
    else:
        category = "肥胖"
    print(f"您的BMI分类为：{category}")
    return BMI


calculate_BMI(70, 1.8)
