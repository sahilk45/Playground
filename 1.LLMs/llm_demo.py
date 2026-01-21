from langchain_openai import OpenAI
from dotenv import load_dotenv     #Loads env variables from .env

load_dotenv()

llm = OpenAI(model='gpt-3.5-turbo-instruct')

result = llm.invoke("What is Capital of India?")

print(result)