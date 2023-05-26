import streamlit as st

import os

from langchain.chat_models import AzureChatOpenAI
from langchain import PromptTemplate, LLMChain
from langchain.chains import SimpleSequentialChain
from langchain.prompts.chat import (
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
    AIMessagePromptTemplate,
    HumanMessagePromptTemplate,
)

from api_key import Az_OpenAI_api_key, Az_OpenAI_endpoint, Az_Open_Deployment_name_gpt35

os.environ["OPENAI_API_TYPE"] = "azure"
os.environ["OPENAI_API_VERSION"] = "2023-03-15-preview"
os.environ["OPENAI_API_BASE"] = Az_OpenAI_endpoint
os.environ["OPENAI_API_KEY"] = Az_OpenAI_api_key

## Set up text input in UX

st.title("Q&A")
prompt = st.text_input("Design a Youtube video")

## Set up OpenAI as chat LLM
chat = AzureChatOpenAI(deployment_name=Az_Open_Deployment_name_gpt35,
            openai_api_version="2023-03-15-preview", temperature=0)

## Title prompt
title_template="You are a helpful designer that helps user to design Youtube video title."
title_system_message_prompt = SystemMessagePromptTemplate.from_template(title_template)

title_human_template="Please design a title about {text}"
title_human_message_prompt = HumanMessagePromptTemplate.from_template(title_human_template)

title_prompt = ChatPromptTemplate.from_messages([title_system_message_prompt, title_human_message_prompt])

## Script prompt
script_template="You are a helpful designer that helps user to design Youtube video script."
script_system_message_prompt = SystemMessagePromptTemplate.from_template(script_template)

script_human_template="Please design a script about {text}"
script_human_message_prompt = HumanMessagePromptTemplate.from_template(script_human_template)

script_prompt = ChatPromptTemplate.from_messages([script_system_message_prompt, script_human_message_prompt])

if prompt:
    title_chain = LLMChain(llm=chat, prompt=title_prompt)
    script_chain = LLMChain(llm=chat, prompt=script_prompt)

    ## Note, we can also run title_chain first and use its response as a parameter passing to script_chain
    sequential_chain = SimpleSequentialChain(chains=[title_chain, script_chain], verbose=True)

    # get a chat completion from the formatted messages
    response = sequential_chain.run(prompt)
    print(response)
    st.write(response)