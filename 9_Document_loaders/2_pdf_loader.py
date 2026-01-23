from langchain_community.document_loaders import PyPDFLoader #pip install pypdf

loader = PyPDFLoader('file_name.pdf')

docs = loader.load()

print(len(docs)) #No. of pages
print(docs[0].page_content)
print(docs[0].metadata)

