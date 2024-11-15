# 基本语法
# class NameOfClass:
#     # 接下来是一些定义类的代码
#     # ...

# 定义可爱猫猫类
class CuteCat:
    # 构造函数，self 表示对象自身
    def __init__(self):
        # 定义猫猫的名字属性，一定要加self，不然会被Python认为是变量
        self.name = "Lambton"


# 创建对象
cat1 = CuteCat()
print(cat1.name)


# 定义可爱猫猫类，构造函数增加参数
class CuteCat2:
    def __init__(self, cat_name):
        self.name = cat_name


# 创建对象
cat1 = CuteCat2("Jojo")
print(cat1.name)


# 定义可爱猫猫类，构造函数增加更多属性
class CuteCat3:
    def __init__(self, cat_name, cat_age, cat_color):
        self.name = cat_name
        self.age = cat_age
        self.color = cat_color


# 创建对象
cat1 = CuteCat3("Jojo", 2, "橙色")
print(f"小猫{cat1.name}的年龄是{cat1.age}岁，花色是{cat1.color}")
