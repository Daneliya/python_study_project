import os

from langchain.agents import AgentType
from langchain.agents import initialize_agent, Tool
from langchain.tools import DuckDuckGoSearchRun
from langchain.utilities import WikipediaAPIWrapper
from langchain_community.chat_models import ChatTongyi

# 设置 DashScope API Key（通义千问）
os.environ["DASHSCOPE_API_KEY"] = "sk-xxxx"  # 替换为你的真实 API Key

# 初始化搜索工具
search = DuckDuckGoSearchRun()
wikipedia = WikipediaAPIWrapper()

# 定义工具集
tools = [
    Tool(
        name="搜索引擎",
        func=search.run,
        description="当你需要查询最新信息时使用这个工具"
    ),
    Tool(
        name="维基百科",
        func=wikipedia.run,
        description="当你需要查询百科知识时使用这个工具"
    )
]

# 初始化通义千问模型（替代 OpenAI）
llm = ChatTongyi(model_name="qwen-max", temperature=0)

# 创建智能体
agent = initialize_agent(
    tools=tools,
    llm=llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True
)

# 执行查询
response = agent.run("bestblogs网站是什么？最近更新是什么时候？")
print(response)
