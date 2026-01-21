from langchain_huggingface import HuggingFaceEndpointEmbeddings
from dotenv import load_dotenv

load_dotenv()

embeddings = HuggingFaceEndpointEmbeddings(
    repo_id="sentence-transformers/all-MiniLM-L6-v2"
)

documents = [
    "Delhi is the capital of India",
    "Chandigarh is the capital of Haryana"
]

vectors = embeddings.embed_documents(documents)
print(len(vectors), len(vectors[0]))
