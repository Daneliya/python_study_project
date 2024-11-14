# 写法
input("这里是给用户的一些提示")
# 定义变量接收用户输入
user_age = input("请输入您的年龄")
print("知道了，你今年" + user_age + "岁了！")

# BMI = 体重 / (身高 ** 2)
user_weight = float(input("请输入您的体重（单位：kg）："))
user_height = float(input("请输入您的身高（单位：m）："))
user_BMI = user_weight / user_height ** 2
print("您的BMI值为：" + str(user_BMI))
