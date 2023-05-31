import os

from langchain.agents import load_tools
from langchain.agents import initialize_agent, Tool
from langchain.agents import AgentType
from langchain.chat_models import AzureChatOpenAI

from api_key import Az_OpenAI_api_key, Az_OpenAI_endpoint, Az_Open_Deployment_name_gpt35
from langchain import LLMMathChain

from tools.tool_price import price_api

os.environ["OPENAI_API_TYPE"] = "azure"
os.environ["OPENAI_API_VERSION"] = "2023-03-15-preview"
os.environ["OPENAI_API_BASE"] = Az_OpenAI_endpoint
os.environ["OPENAI_API_KEY"] = Az_OpenAI_api_key

# Check the existence of tools
print(price_api)

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
    Tool(
        name="Calculator",
        func=llm_math_chain.run,
        description="useful for when you need to answer questions about math",
        return_direct=True
    )
]

agent = initialize_agent(tools, chat, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True)

response = agent.run("How much are four good year tires?")

print(response)