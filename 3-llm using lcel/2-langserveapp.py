# install fastapi in envi
# install uvicorn
# install langserve
# install all other packages

# load envi variables
import os
from dotenv import load_dotenv
load_dotenv()

# using groq
from langchain_groq import ChatGroq
groq_api_key = os.getenv("GROQ_API_KEY")
llm_groq1 = ChatGroq(model='Gemma2-9b-It',groq_api_key=groq_api_key)

# setting prompt
from langchain_core.prompts import ChatPromptTemplate
system_template = "translate the following into {language}"
prompt_template = ChatPromptTemplate.from_messages(
    [
        ("system",system_template),
        ("user","{input_text}")
    ])

# setting outputparser
from langchain_core.output_parsers import StrOutputParser
op_parser1 = StrOutputParser()

# creating chain
chain = prompt_template|llm_groq1|op_parser1

# using fastapi
from fastapi import FastAPI
app=FastAPI(title="langchain server : langserve",
            version="1.1",
            description="simple langchain server using langchain runnable interfaces")

# using langserve
from langserve import add_routes # add_routes helps to create apis
add_routes(
    app,
    chain,
    path='/chain'
)

# uvicorn is webserver to recieve reqs from apps and send responses
if __name__=="__main__":
    import uvicorn
    uvicorn.run(app,host="localhost",port=8000)

# to run app use python filename.py
# write /docs after the url after running
