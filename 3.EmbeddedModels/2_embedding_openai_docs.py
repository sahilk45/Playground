from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

embedding = OpenAIEmbeddings(model='text-embedding-3-large',dimensions=32)

documents = [
    "Delhi is the capital of India",
    "Chandigarh is the capital of Haryana",
    "India lies in south-asia"
]

result = embedding.embed_documents(documents) #will give 2D list, every list is one document

print(str(result))