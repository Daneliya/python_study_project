# 普通函数
def calculate_and_print(num, power):
    if power == 2:
        result = num * num
    elif power == 3:
        result = num * num * num
    else:
        print("只支持计算二次方和三次方")
        return
    print(f"""
    | 数字参数 | {num} |
    | 计算结果 | {result} |""")


calculate_and_print(3, 3)


# 改造后
def calculate_and_print(num, calculator):
    result = calculator(num)
    print(f"""
    | 数字参数 | {num} |
    | 计算结果 | {result} |""")


def calculate_square(num):
    return num * num


def calculate_cube(num):
    return num * num * num


def calculate_plus_10(num):
    return num + 10


def calculate_times_5(num):
    return num * 5


calculate_and_print(3, calculate_square)
calculate_and_print(7, calculate_plus_10)
calculate_and_print(7, calculate_times_5)


# 进一步改造，把格式作为参数，扩展不同打印格式
def calculate_and_print(num, calculator, formatter):
    result = calculator(num)
    formatter(num, result)


def print_with_vertical_bar(num, result):
    print(f"""
    | 数字参数 | {num} |
    | 计算结果 | {result} |""")


calculate_and_print(7, calculate_times_5, print_with_vertical_bar)
