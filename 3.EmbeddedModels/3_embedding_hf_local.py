from langchain_huggingface import HuggingFaceEmbeddings

embedding=HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

# text= " Delhi is capital of india"
# vector = embedding.embed_query(text)

documents = [
    "Delhi is the capital of India",
    "Chandigarh is the capital of Haryana",
    "India lies in south-asia"
]

vector = embedding.embed_documents(documents)

print(str(vector))