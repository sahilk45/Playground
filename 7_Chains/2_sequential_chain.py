from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

model = ChatGoogleGenerativeAI(model='gemini-3-flash-preview')

prompt1 = PromptTemplate(
    template='Generative a detailed report on {topic}',
    input_variables=['topic']
)

prompt2=PromptTemplate(
    template='Generate a 3 pointer summary for following text \n {text}',
    input_variables=['text']
)

parser = StrOutputParser()

chain = prompt1 | model | parser | prompt2 | model | parser
result = chain.invoke({'topic':'Tourism in India'})
print(result)

chain.get_graph.print_ascii()