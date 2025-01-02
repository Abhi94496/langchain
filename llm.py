#contains how to initiate the model and how to get the diffrent styles of output

from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os
load_dotenv() 
# openai_api_key = os.getenv("OPENAI_API_KEY")
# print(openai_api_key)
llm = ChatOpenAI()

#case1
response = llm.stream("i am planning to the go trek")
for chunk in response:
    print(chunk.content, end= "", flush= True)

#case2
response = llm.invoke("i am planning to the go trek")
print(response)

#case3
response = llm.batch(["hi , good morning","i am planning to the go trek"])
print(response)