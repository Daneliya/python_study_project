# 定义对象中的方法
class CuteCat:
    def __init__(self, cat_name, cat_age, cat_color):
        self.name = cat_name
        self.age = cat_age
        self.color = cat_color

    def speak(self):
        print("喵" * self.age)

    def think(self, content):
        print(f"小猫{self.name}在思考{content}...")


cat1 = CuteCat("Jojo", 3, "橙色")
cat1.speak()
cat1.think("现在去抓沙发还是去撕纸箱")


# 实践
# 定义一个学生类
# 要求：
# 1. 属性包括学生姓名、学号，以及语数英三科成绩
# 2. 能够设置学生某科目的成绩
# 3. 能够打印出该学生所有科目的成绩

class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.grades = {"语文": 0, "数学": 0, "英语": 0}

    def set_grade(self, course, grade):
        if course in self.grades:
            self.grades[course] = grade

    def print_grades(self):
        print(f"学生{self.name}（学号：{self.student_id}）的成绩为：")
        for course in self.grades:
            print(f"{course}：{self.grades[course]}分")


chen = Student("小陈", "100618")
print(chen.name)
zeng = Student("小曾", "100622")
zeng.set_grade("语文", 92)
zeng.set_grade("数学", 94)
zeng.print_grades()
