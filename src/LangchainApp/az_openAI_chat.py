import os

from langchain.chat_models import AzureChatOpenAI
from langchain.schema import (
    AIMessage,
    HumanMessage,
    SystemMessage
)

from api_key import Az_OpenAI_api_key, Az_OpenAI_endpoint, Az_Open_Deployment_name_gpt35

os.environ["OPENAI_API_TYPE"] = "azure"
os.environ["OPENAI_API_VERSION"] = "2023-03-15-preview"
os.environ["OPENAI_API_BASE"] = Az_OpenAI_endpoint
os.environ["OPENAI_API_KEY"] = Az_OpenAI_api_key

chat = AzureChatOpenAI(deployment_name=Az_Open_Deployment_name_gpt35,
            openai_api_version="2023-03-15-preview", temperature=0)

response = chat([HumanMessage(content="Translate this sentence from English to French. I love programming.")])

print(response.content)

messages = [
    SystemMessage(content="You are a helpful assistant that helps user to find information."),
    HumanMessage(content="What is the most important event happened in 1986?")
]

response = chat(messages)

print(response.content)

from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
chat_stream = AzureChatOpenAI(deployment_name=Az_Open_Deployment_name_gpt35,
            openai_api_version="2023-03-15-preview", 
            streaming=True, callbacks=[StreamingStdOutCallbackHandler()], temperature=0)
resp = chat_stream([HumanMessage(content="Write me a song about sparkling water.")])

print(resp)