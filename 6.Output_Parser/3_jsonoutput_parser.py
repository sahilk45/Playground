from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser

load_dotenv()

llm=HuggingFaceEndpoint(
    repo_id="HuggingFaceH4/zephyr-7b-beta",
    task="text-generation"
)

model = ChatHuggingFace(llm=llm)

parser = JsonOutputParser()

template = PromptTemplate(
    template='Give me name, age and city of a fictional person.\n {format_instruction}',
    input_variables=[],
    partial_variables={'format_instruction':parser.get_format_instructions()}
    #partial var beac filled before runtime
)

# prompt = template.format()

# result = model.invoke(prompt)

# final_result = parser.parse(result.content)

#can make chain instead:
chain = template | model | parser
final_result = chain.invoke({})

print(final_result)
print(final_result['name'])
print(type(final_result)) #in py json is a dict