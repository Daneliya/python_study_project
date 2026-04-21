import os

from langchain_classic.chains import RetrievalQA
from langchain_community.vectorstores import Chroma
from langchain_community.chat_models import ChatTongyi
from langchain_community.document_loaders import TextLoader
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_text_splitters import CharacterTextSplitter

os.environ["DASHSCOPE_API_KEY"] = "sk-xxxxx"  # 替换为你的真实 API Key

# 加载文档
loader = TextLoader("新闻介绍.txt", encoding="utf-8")
documents = loader.load()

# 分割文档
text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
texts = text_splitter.split_documents(documents)

# 使用 huggingface 的 embedding
embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2"
)

# 创建向量数据库
db = Chroma.from_documents(texts, embeddings)

# 使用通义千问 LLM
llm = ChatTongyi(model_name="qwen3.6-plus")

# 构建问答链
qa = RetrievalQA.from_chain_type(
    llm=llm,
    chain_type="stuff",
    retriever=db.as_retriever()
)

query = "中国青年网民对 AI 社交有什么看法？"
result = qa.run(query)
print(result)
