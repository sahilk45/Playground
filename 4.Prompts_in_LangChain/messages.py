from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.messages import SystemMessage,HumanMessage,AIMessage

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-3-flash-preview")

messages=[
    SystemMessage(content='You are a helpful assistant'),
    HumanMessage(content='Tell me about LangChain')
]

result=model.invoke(messages)

messages.append(AIMessage(content=result.text))

print(messages)