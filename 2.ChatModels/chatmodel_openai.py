from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI(model='gpt-4',
                   temparature=1.0,max_completion_tokens=50)

result = model.invoke("What is capital of India?")

print(result.content)