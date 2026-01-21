from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

embedding = OpenAIEmbeddings(model='text-embedding-3-large',dimensions=32)

#can generate single query embedding
result = embedding.embed_query("Delhi is capital of India")

print(str(result))