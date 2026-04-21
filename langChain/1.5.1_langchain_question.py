import os

from langchain.chains import RetrievalQAWithSourcesChain
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.chat_models import ChatTongyi
from langchain_community.document_loaders import DirectoryLoader
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings

# 设置通义千问 API Key
os.environ["DASHSCOPE_API_KEY"] = "sk-xxxxx"  # 替换为你的真实 API Key

# 加载文档
loader = DirectoryLoader("./data/", glob="**/*.md")
documents = loader.load()

# 文档分割
text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
texts = text_splitter.split_documents(documents)

# 创建向量数据库，使用 HuggingFace Embeddings 替代 OpenAI Embeddings
embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2"
)
vectorstore = FAISS.from_documents(texts, embeddings)

# 创建问答链，LLM 使用通义千问 qwen-max
llm = ChatTongyi(model_name="qwen3.6-plus", temperature=0)
chain = RetrievalQAWithSourcesChain.from_chain_type(
    llm=llm,
    chain_type="stuff",
    retriever=vectorstore.as_retriever()
)

# 运行查询
query = "如何使用面试鸭网站准备技术面试？"
result = chain({"question": query})

print(f"回答: {result['answer']}")
print(f"来源: {result['sources']}")
