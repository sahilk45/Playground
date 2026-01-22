from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from typing import TypedDict,Annotated,Optional,Literal

load_dotenv()

model = ChatGoogleGenerativeAI(model='gemini-3-flash-preview')

#schema
class Review(TypedDict):
    key_themes:Annotated[str,"Write down all the keys discussed in the review in a list"]
    summary:Annotated[str, "A breif summary of the review"]
    sentiment:Annotated[Literal["pos","neg"],"Return sentiment of review either positive,negative or neutral"]
    pros:Annotated[Optional[list[str]],"Write down all the pros inside a list"]
    cons:Annotated[Optional[list[str]],"Write down all the cons inside a list"]
    name:Annotated[Optional[str],"Write the name of reviewer"]

structured_model = model.with_structured_output(Review)

result = structured_model.invoke(""" . . """)

print(result)  #is a dictionary
print(result['summary'])
print(result['sentiment'])
