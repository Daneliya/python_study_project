# 定义原txt文件路径（把你的文件路径替换这里）
file_path = "文本.txt"

try:
    # 1. 读取原文件内容
    with open(file_path, "r", encoding="utf-8") as f:
        text = f.read()

    # 2. 按标点符号分割句子
    split_chars = ["，", "。", "？"]
    current_sentence = ""
    result = []

    for char in text:
        current_sentence += char
        # 遇到分割标点就切分
        if char in split_chars:
            sentence = current_sentence.strip()
            if sentence:
                result.append(sentence)
            current_sentence = ""

    # 3. 生成新文件名：原文件名 + "_文本分割.txt"
    # 拆分文件名和后缀（例如 文本.txt → 文本 和 .txt）
    file_name = file_path.rsplit(".", 1)[0]
    new_file_path = f"{file_name}_文本分割.txt"

    # 4. 写入新文件
    with open(new_file_path, "w", encoding="utf-8") as f:
        f.write("\n".join(result))

    # 控制台提示
    print(f"✅ 分割完成！")
    print(f"📄 新文件已保存为：{new_file_path}")
    print("\n预览输出内容：")
    print("-" * 30)
    print("\n".join(result))

except FileNotFoundError:
    print(f"❌ 错误：未找到文件 {file_path}，请检查文件路径！")
except Exception as e:
    print(f"❌ 发生错误：{e}")