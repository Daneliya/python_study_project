year = "虎"
name = "小明"

# format 方法，指定替换位置
message_content = """
新岁甫至，福气东来。
金{0}贺岁，欢乐祥瑞。
金{0}敲门，五福临门。
给{1}及家人拜年啦!
新春快乐，{0}年大吉!
""".format(year, name)
print(message_content)

# format 方法，指定替换对象
message_content = """律回春渐，新元肇启。
新岁甫至，福气东来。
金{current_year}贺岁，欢乐祥瑞。
金{current_year}敲门，五福临门。
给{current_name}及家人拜年啦!
新春快乐，{current_year}年大吉!
""".format(current_year=year, current_name=name)
print(message_content)

# f 字符串
current_year = "虎"
current_name = "王"
message_content = f"""律回春渐，新元肇启。
新岁甫至，福气东来。
金{current_year}贺岁，欢乐祥瑞。
金{current_year}敲门，五福临门。
给{current_name}及家人拜年啦!
新春快乐，{current_year}年大吉!
"""
print(message_content)

# 数字对字符串进行格式化
gpa_dict = {"小明": 3.251, "小花": 3.869, "小李": 2.683, "小张": 3.685}
for name, gpa in gpa_dict.items():
    print("{0}你好，你的当前绩点为：{1:.2f}".format(name, gpa))
print("=====================")
for name, gpa in gpa_dict.items():
    print(f"{name}你好，你的当前绩点为：{gpa:.2f}")
