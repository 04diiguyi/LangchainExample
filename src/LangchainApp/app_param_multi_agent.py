import os

from langchain.agents import initialize_agent, Tool, AgentType
from langchain.tools import StructuredTool
from langchain.chat_models import AzureChatOpenAI

from api_key import Az_OpenAI_api_key, Az_OpenAI_endpoint, Az_Open_Deployment_name_gpt35
from langchain import LLMMathChain

from tools.tool_price import price_api
from tools.tool_inventory import inventory_api

os.environ["OPENAI_API_TYPE"] = "azure"
os.environ["OPENAI_API_VERSION"] = "2023-03-15-preview"
os.environ["OPENAI_API_BASE"] = Az_OpenAI_endpoint
os.environ["OPENAI_API_KEY"] = Az_OpenAI_api_key

# Check the existence of tools
print(price_api)
print(inventory_api)

## Set up OpenAI as chat LLM
chat = AzureChatOpenAI(deployment_name=Az_Open_Deployment_name_gpt35,
            openai_api_version="2023-03-15-preview", temperature=0)

llm_math_chain = LLMMathChain(llm=chat)

tools = [
    Tool(
        name = "Search Price",
        func=price_api.run,
        description="useful for when you need to answer the price of tires"
    ),
    StructuredTool.from_function(inventory_api),
    Tool(
        name="Calculator",
        func=llm_math_chain.run,
        description="useful for when you need to answer questions about math",
        return_direct=True
    )
]

agent = initialize_agent(tools, chat, agent=AgentType.STRUCTURED_CHAT_ZERO_SHOT_REACT_DESCRIPTION , verbose=True)

response = agent.run("I want to buy four good year tires in my local Issaquah store, \
                     do we have enough in stock and how much is the total price?")

print(response)

response = agent.run("I want to buy 30 good year tires in my local Issaquah store, \
                     do we have enough in stock and how much is the total price?")

print(response)