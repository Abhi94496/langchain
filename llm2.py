from dotenv import load_dotenv
load_dotenv()

from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate

from langchain_core.output_parsers import StrOutputParser, CommaSeparatedListOutputParser, JsonOutputParser


from pydantic import BaseModel, Field


model = ChatOpenAI(model="gpt-3.5-turbo", temperature= 0.4)

###########################################################################
#getting response output in string format

# def call_string_output_parser():
#     prompt  = ChatPromptTemplate.from_messages([("system, Tell me joke about the following subject"),
#                                             ("human,{input}")])
#     parser = StrOutputParser()

#     chain = prompt | model | parser
#     return chain.invoke({"input" : "tree"})

# print(call_string_output_parser())
# print(type(call_string_output_parser()))
#------------------------------------------------------------------------------

# def call_list_output_parser():
#     prompt = ChatPromptTemplate.from_messages([ ("system, i need list of 10 words for the folowing topic"),
#                                                ("human, {input}")])
#     parser = CommaSeparatedListOutputParser()

#     chain = prompt | model | parser

#     return chain.invoke({"input" : "india"})

# print(call_list_output_parser())

#---------------------------------------------------------------------------------

def json_output_parser():
    prompt = ChatPromptTemplate.from_messages([
        ("system", "i need to extract the info from following phrase.\n formating instructions : {format_inst}"),
        ("human", "{phrase}")
         ])
    class person(BaseModel):
        name : str = Field(description= "name of the person")
        age : int = Field(description="age of the person")

    parser  = JsonOutputParser(pydantic_object=person)

    chain = prompt | model | parser
    return chain.invoke({"phrase" : " i am abhishek and i am 20 years old ",
                        "format_inst" : parser.get_format_instructions()})

print(json_output_parser())
