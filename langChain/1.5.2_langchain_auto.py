import os

from langchain.agents import AgentType
from langchain.agents import initialize_agent, Tool
from langchain.memory import ConversationBufferMemory
from langchain.utilities import SerpAPIWrapper, PythonREPL
from langchain_community.chat_models import ChatTongyi

# 设置通义千问 API Key
os.environ["DASHSCOPE_API_KEY"] = "sk-xxxxx"

# 初始化工具
search = SerpAPIWrapper()
python_repl = PythonREPL()

tools = [
    Tool(
        name="搜索引擎",
        func=search.run,
        description="用于查询最新信息"
    ),
    Tool(
        name="Python执行器",
        func=python_repl.run,
        description="可以执行Python代码进行数据分析"
    )
]

# 设置记忆组件
memory = ConversationBufferMemory(memory_key="chat_history")

# 初始化通义千问 LLM 替代 OpenAI
llm = ChatTongyi(model_name="qwen-max", temperature=0)

# 创建智能体
agent = initialize_agent(
    tools=tools,
    llm=llm,
    agent=AgentType.CONVERSATIONAL_REACT_DESCRIPTION,
    memory=memory,
    verbose=True
)

# 运行智能体
response = agent.run("我想分析编程导航网站的用户增长数据，可以帮我写一个简单的Python脚本吗？")
print(response)
