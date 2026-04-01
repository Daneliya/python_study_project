try:  # 有可能产生错误的代码
    user_weight = float(input("请输入您的体重（单位：kg）："))
    user_height = float(input("请输入您的身高（单位：m）："))
    user_BMI = user_weight / user_height ** 2
except ValueError:  # 产生值错误时会运行
    print("输入不为合理数字，请重新运行程序，并输入正确的数字。")
except ZeroDivisionError:  # 产生除零错误时会运行
    print("身高不能为零，请重新运行程序，并输入正确的数字。")
except:  # 产生其它错误时会运行
    print("发生了未知错误，请重新运行程序。")
else:  # 没有错误时会运行
    print("您的BMI值为：" + str(user_BMI))
finally:  # 不管发生错误与否都会运行
    print("程序结束运行。")
