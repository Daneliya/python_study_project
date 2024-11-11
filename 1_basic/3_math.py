import math

# 一元二次求根公式计算器
a = -1
b = -2
c = 3
print((-b + (b ** 2 - 4 * a * c) ** (1 / 2)) / (2 * a))
print((-b - (b ** 2 - 4 * a * c) ** (1 / 2)) / (2 * a))

print((-b + math.sqrt(b ** 2 - 4 * a * c)) / (2 * a))
print((-b - math.sqrt(b ** 2 - 4 * a * c)) / (2 * a))

delta = b ** 2 - 4 * a * c
print((-b + math.sqrt(delta)) / (2 * a))
print((-b - math.sqrt(delta)) / (2 * a))
