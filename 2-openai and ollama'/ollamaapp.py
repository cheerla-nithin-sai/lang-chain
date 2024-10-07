## using ollama
# Ollama is a free and open-source tool that lets anyone run open LLMs locally on your system
import os
from dotenv import load_dotenv
load_dotenv()
# to load env variables

from langchain_community.llms import Ollama 
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

# langsmith tracking
os.environ["LANGCHAIN_API_KEY"] = os.getenv('LANGCHAIN_API_KEY')
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_PROJECT"] = os.getenv("LANGCHAIN_PROJECT3")


# prompt template
prompt = ChatPromptTemplate.from_messages([
    ("system","you are expert in predicting the silver prices"),
    ("user","Question:{question}")
])

# streamlit framework
import streamlit as st
st.title("Langchain demo with gemma 2b")
input_text = st.text_input("what question you have about silver?")

# initializing the moodel from ollama
llm_1 = Ollama(model='gemma:2b')
output_parser = StrOutputParser()

chain = prompt | llm_1 | output_parser

if input_text:
    st.write(chain.invoke({"question":input_text}))