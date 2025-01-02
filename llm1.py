#in this contains that  how to pass the prompts in diffrent format 

from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os
from langchain_core.prompts import ChatPromptTemplate
load_dotenv() 



# openai_api_key = os.getenv("OPENAI_API_KEY")
# print(openai_api_key)

#initiate
llm = ChatOpenAI(model= "gpt-3.5-turbo", temperature= 0.4)

##############################################
#types of prompt input

# prompt = ChatPromptTemplate.from_template("tell me a joke about {topic}")

prompt = ChatPromptTemplate.from_messages([
    ("system","you are an quiz master i need the 3 questions with 4 options for the following topic, and return the output in the json format "),
    ("human", "{topic}")
    ])
###############################################
chain = prompt | llm
response = chain.stream({"topic" : "india"})
# print(response)

for chunk in response:
    print(chunk.content, end= "", flush= True)

###############################################
