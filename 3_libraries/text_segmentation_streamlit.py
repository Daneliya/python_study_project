# Streamlit 文本分割工具（增强版）
# 功能：上传、在线编辑、一键下载、深色模式切换、清空按钮、字数统计、分割后自动去除句尾标点
# 运行方式
# 1. 安装依赖
# pip install streamlit
# 2. 运行
# streamlit run text_split_app.py


import streamlit as st
import os

# ---------------------- 页面配置 ----------------------
st.set_page_config(
    page_title="TXT 文本分句分割工具",
    layout="wide",
    initial_sidebar_state="collapsed"
)


# ---------------------- 分割逻辑（新版：去掉句尾标点） ----------------------
def split_text_content(text):
    # 分句结束标点
    end_punct = ["，", "。", "？", "；", "："]
    current_sentence = ""
    result = []
    for char in text:
        current_sentence += char
        if char in end_punct:
            # 去除首尾空白 + 去掉最后一个标点
            sentence = current_sentence.strip()
            if sentence:
                # 删掉末尾的标点符号
                if sentence[-1] in end_punct:
                    sentence = sentence[:-1].strip()
                if sentence:
                    result.append(sentence)
            current_sentence = ""
    return "\n".join(result)


# ---------------------- 初始化session状态 ----------------------
if "edit_text" not in st.session_state:
    st.session_state.edit_text = ""
if "upload_filename" not in st.session_state:
    st.session_state.upload_filename = ""

# ---------------------- 深色模式切换 ----------------------
st.sidebar.title("设置")
dark_mode = st.sidebar.toggle("🌙 深色模式", value=False)

# 注入深色模式CSS
if dark_mode:
    st.markdown("""
    <style>
    .stApp {background-color: #1e1e1e; color: #f0f0f0;}
    textarea {background-color: #2d2d2d !important; color: #f0f0f0 !important;}
    </style>
    """, unsafe_allow_html=True)

# ---------------------- 标题与上传 ----------------------
st.title("📝 TXT 文本分句分割工具")
st.markdown("上传TXT → 自动分句去标点 → 在线编辑 → 一键下载")

st.subheader("✅ 选择 TXT 文件")
# uploaded_file = st.file_uploader("选择 TXT 文件", type="txt")
uploaded_file = st.file_uploader("", type="txt")

# 上传文件处理
if uploaded_file is not None:
    raw_text = uploaded_file.read().decode("utf-8")
    # 分割处理
    split_result = split_text_content(raw_text)
    # 存入会话状态
    st.session_state.edit_text = split_result
    st.session_state.upload_filename = uploaded_file.name

# ---------------------- 功能按钮行 ----------------------
col1, col2 = st.columns([1, 1])
with col1:
    clear_btn = st.button("🗑️ 清空内容", use_container_width=True)
with col2:
    pass

# 清空按钮逻辑
if clear_btn:
    st.session_state.edit_text = ""

# ---------------------- 可编辑文本框 ----------------------
st.subheader("✅ 分割结果（可直接编辑修改）")
edit_text = st.text_area(
    label="编辑区域",
    value=st.session_state.edit_text,
    height=400,
    label_visibility="collapsed"
)
# 同步更新到会话
st.session_state.edit_text = edit_text

# ---------------------- 字数统计 ----------------------
total_chars = len(edit_text.replace("\n", ""))
line_count = len([line for line in edit_text.splitlines() if line.strip()])
st.info(f"📊 总行数：{line_count} 行 ｜ 总字符数（不含换行）：{total_chars} 字")

# ---------------------- 下载按钮 ----------------------
if st.session_state.upload_filename:
    original_name = st.session_state.upload_filename
    name, ext = os.path.splitext(original_name)
    download_filename = f"{name}_文本分割.txt"

    st.download_button(
        label="💾 下载处理好的文件",
        data=edit_text.encode("utf-8"),
        file_name=download_filename,
        mime="text/plain",
        use_container_width=True
    )
