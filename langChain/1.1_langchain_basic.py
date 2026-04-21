import os

from langchain_community.chat_models import ChatTongyi
from langchain_core.prompts import PromptTemplate

# 设置通义千问的 API Key
os.environ["DASHSCOPE_API_KEY"] = "sk-xxxxxx"  # 替换为你的真实 API Key

# 1. 定义 Prompt 模板
prompt = PromptTemplate.from_template(
    "你是一个知识渊博的助手，请用简洁的方式回答问题：{question}"
)

# 2. 加载通义千问模型
llm = ChatTongyi(
    model_name="qwen3.6-plus",
    temperature=0.7,
)

# 3. 构建 chain：Prompt + LLM，符合 Runnable 架构
chain = prompt | llm

# 4. 调用推理（新版：使用 invoke）
response = chain.invoke({"question": "你好，我是精灵王鸭吉吉，请介绍一下LangChain。"})

# 5. 输出结果
print(response.content)
