import os
import tkinter as tk
from tkinter import filedialog, scrolledtext

def split_text_content(text):
    """按中文标点 ，。？ 分割句子"""
    split_chars = ["，", "。", "？"]
    current_sentence = ""
    result = []
    for char in text:
        current_sentence += char
        if char in split_chars:
            sentence = current_sentence.strip()
            if sentence:
                result.append(sentence)
            current_sentence = ""
    return "\n".join(result)

def select_file():
    """选择txt文件"""
    global raw_file_path
    file_path = filedialog.askopenfilename(
        filetypes=[("文本文件", "*.txt"), ("所有文件", "*.*")]
    )
    if not file_path:
        return
    raw_file_path = file_path
    # 读取文件
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()
    # 分割
    split_content = split_text_content(content)
    # 清空并插入分割后的内容
    text_box.delete(1.0, tk.END)
    text_box.insert(tk.END, split_content)

def save_file():
    """保存为 原文件名_文本分割.txt"""
    if not raw_file_path:
        tk.messagebox.showwarning("提示", "请先选择TXT文件！")
        return
    # 获取编辑后的内容
    edit_content = text_box.get(1.0, tk.END).strip()
    # 构造新文件名
    dir_name, full_name = os.path.split(raw_file_path)
    name, ext = os.path.splitext(full_name)
    new_name = f"{name}_文本分割.txt"
    new_path = os.path.join(dir_name, new_name)
    # 写入
    with open(new_path, "w", encoding="utf-8") as f:
        f.write(edit_content)
    tk.messagebox.showinfo("完成", f"已保存成功！\n{new_path}")

# 主界面
root = tk.Tk()
root.title("TXT文本分句分割工具")
root.geometry("700x500")

raw_file_path = ""

# 按钮区域
frame_top = tk.Frame(root)
frame_top.pack(pady=10)

btn_select = tk.Button(frame_top, text="选择TXT文件", command=select_file, width=15, height=2)
btn_select.grid(row=0, column=0, padx=10)

btn_save = tk.Button(frame_top, text="下载保存文件", command=save_file, width=15, height=2)
btn_save.grid(row=0, column=1, padx=10)

# 可编辑文本框
tk.Label(root, text="分割结果（可手动修改）：").pack()
text_box = scrolledtext.ScrolledText(root, width=85, height=25, font=("微软雅黑", 11))
text_box.pack(padx=10, pady=5)

root.mainloop()