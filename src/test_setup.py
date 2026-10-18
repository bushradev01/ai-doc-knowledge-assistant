from dotenv import load_dotenv
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_community.vectorstores import FAISS

load_dotenv()

# Test 1: OpenAI chat call
llm = ChatOpenAI(model="gpt-4o-mini")
print("LLM test:", llm.invoke("Say hello in 5 words").content)

# Test 2: small FAISS index
texts = ["Acme Cloud supports SSO login.", "Backups run every night at 2 AM."]
db = FAISS.from_texts(texts, OpenAIEmbeddings())
result = db.similarity_search("When do backups happen?", k=1)
print("FAISS test:", result[0].page_content)