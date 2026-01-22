from langchain_core.prompts import ChatPromptTemplate

#create dynamic prompts
chat_template=([
    ('system','You are a helpful {domain} expert'),
    ('Human','Explain in simple words what is {topic}')
])

prompt=chat_template.invoke({'domain':'cricket','topic':'lbw'})

print(prompt)