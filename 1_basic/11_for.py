# for循环写法格式
# for 变量名 in 可迭代对象:
#     # 对每个变量做一些事情
#     # ...

# 列表循环
temperature_list = [36.4, 36.6, 36.2, 38.0]
for temperature in temperature_list:
    if temperature >= 38:
        print(temperature)
        print("完球了")

# 字典循环
temperature_dict = {"111": 36.4, "112": 36.6, "113": 36.2, "114": 38.0}
for staff_id, temperature in temperature_dict.items():
    if temperature >= 38:
        print(staff_id)

# 字典循环
temperature_dict = {"111": 36.4, "112": 36.6, "113": 36.2, "114": 38.0}
for temperature_tuple in temperature_dict.items():
    staff_id = temperature_tuple[0]
    temperature = temperature_tuple[1]
    if temperature >= 38:
        print(staff_id)

# for 结合 range
for i in range(5, 10):
    print(i)  # 打印5到9，不包括10

# for 结合 range(起始值, 结束值, 步长)
for i in range(5, 10, 2):
    print(i)  # 打印5、7、9

# 计算1到100，秒杀高斯
total = 0
for i in range(1, 100):
    total = total + i
print("1到100的和为：" + str(total))
