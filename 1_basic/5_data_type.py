# 字符串 str
# 整数 int
# 浮点数 float
# 布尔类型 bool
# 空值类型 NoneType
# 字符串 str

# 对字符串求长度
s = "hello world!"
print(len(s))

# 通过索引获取单个字符
print(s[0])
print(s[11])
print(s[len(s) - 1])

# 布尔类型
b1 = True
b2 = False

# 空值类型
n = None

# type函数
print(type(s))
print(type(b1))
print(type(n))
print(type(1.5))

# 错误测试：对布尔类型使用len函数
len(b1)