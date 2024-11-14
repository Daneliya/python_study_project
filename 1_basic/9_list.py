# 定义一个空列表
shopping_list = []
# 添加数据
shopping_list.append("键盘")
shopping_list.append("键帽")
print(shopping_list)
# 删除数据
shopping_list.remove("键帽")
print(shopping_list)

shopping_list.append("音箱")
shopping_list.append("电竞椅")
# 覆盖指定下标的数据
shopping_list[1] = "硬盘"
print(shopping_list)
print(len(shopping_list))
print(shopping_list[0])

price = [799, 1024, 200, 800]
# 列表中的最大值
max_price = max(price)
# 列表中的最小值
min_price = min(price)
# 列表排序
socket_price = sorted(price)
print(max_price)
print(min_price)
print(socket_price)
