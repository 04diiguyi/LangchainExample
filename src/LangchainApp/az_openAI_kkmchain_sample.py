from api_key import Az_OpenAI_api_key, Az_OpenAO_endpoint, Az_Open_Deployment_name_gpt3

import os

from langchain.llms import AzureOpenAI
from langchain import PromptTemplate, LLMChain

os.environ["OPENAI_API_TYPE"] = "azure"
os.environ["OPENAI_API_VERSION"] = "2022-12-01" #"2023-05-15"
os.environ["OPENAI_API_BASE"] = Az_OpenAO_endpoint
os.environ["OPENAI_API_KEY"] = Az_OpenAI_api_key

# Create an instance of Azure OpenAI
# Replace the deployment name with your own
llm = AzureOpenAI(
    deployment_name=Az_Open_Deployment_name_gpt3,
    model_name="text-davinci-003", 
)

template = """Question: {question}

Answer: Let's think step by step."""

prompt = PromptTemplate(template=template, input_variables=["question"])

llm_chain = LLMChain(prompt=prompt, llm=llm)

question = "What NFL team won the Super Bowl in the year Justin Beiber was born?"

result = llm_chain.run(question)

print(result)
