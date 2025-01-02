import os
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain.chains import RetrievalQA
from langchain_openai import ChatOpenAI
from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
load_dotenv()

# Step 1: Load the PDF
pdf_path = "Doctrine_of_bonafide_purchaser.pdf"  # Replace with your PDF file path
loader = PyPDFLoader(pdf_path)
documents = loader.load()

# Step 2: Split the content into chunks
text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
texts = text_splitter.split_documents(documents)

# Step 3: Create embeddings and store in FAISS
embedding = OpenAIEmbeddings()  # Uses OpenAI embeddings
vectorstore = FAISS.from_documents(texts, embedding)

# retrieved_chunks = vectorstore.similarity_search(query, k=3)
# # Display the retrieved chunks
# for i, chunk in enumerate(retrieved_chunks, 1):
#     print(f"Chunk {i}:\n{chunk.page_content}\n")


# Step 4: Convert FAISS to a retriever
retriever = vectorstore.as_retriever(search_kwargs={"k": 3})  # Retrieve top 3 matches

# Step 5: Initialize the OpenAI LLM
llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0.5)

# Step 6: Create a RetrievalQA chain
qa_chain = RetrievalQA.from_chain_type(llm=llm, retriever=retriever)


# Step 7: Query the system
instruction = "You are a helpful legal assistant. give the output in json format"
query = " what is quote said by vikram nath j in the judgement"
# Combine instruction and query
prompt = f"{instruction}\n\nQuery: {query}"
response = qa_chain.invoke(prompt)


# Step 8: Display the response
print("Response:")
print(response)