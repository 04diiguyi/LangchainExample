import os
import json

from langchain.chat_models import AzureChatOpenAI
from langchain import LLMChain
from langchain.prompts.chat import (
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate
)

from api_key import Az_OpenAI_api_key, Az_OpenAI_endpoint, Az_Open_Deployment_name_gpt35

class Car_inventory_Info:
    """class contains car information"""
    def __init__(self, id, name, color, drive, inventory, extra_info):
        self.id = id
        self.name = name
        self.color = color
        self.drive = drive
        self.inventory = inventory
        self.extra_info = extra_info


os.environ["OPENAI_API_TYPE"] = "azure"
os.environ["OPENAI_API_VERSION"] = "2023-03-15-preview"
os.environ["OPENAI_API_BASE"] = Az_OpenAI_endpoint
os.environ["OPENAI_API_KEY"] = Az_OpenAI_api_key

chat = AzureChatOpenAI(deployment_name=Az_Open_Deployment_name_gpt35,
            openai_api_version="2023-03-15-preview", temperature=0)

opening_sentense = "You are a json translator that translates a json string to a human readable sentence. "
detail_message1 = "If field `drive` is `A`, it means all wheel drive, if field `drive` is `F`, it means front wheel drive, if field `drive` is `R`, it means rear wheel drive."
detail_message2 = "If field `inventory` is `Stock` it means the vehicle is available in stock, if field `inventory` is `Transit`, it means the vehicle is in transit, if field `inventory` is an integer, it means the buyer needs to wait for that amount of months to get the vehicle."
detail_message2 = "If field `extra_info` is `rim` it means we need rim size from the customer, if field `extra_info` is `None`, it means we do not need extra information, if field `extra_info` is `body`, it means we need car body information."
template=opening_sentense + detail_message1 + detail_message2
system_message_prompt = SystemMessagePromptTemplate.from_template(template)
human_template="{text}"
human_message_prompt = HumanMessagePromptTemplate.from_template(human_template)

chat_prompt = ChatPromptTemplate.from_messages([system_message_prompt, human_message_prompt])
chain = LLMChain(llm=chat, prompt=chat_prompt)
# get a chat completion from the formatted messages

# Car with ID 001 is a White Ford with front wheel drive and is currently in stock. No extra information is needed.
car_inventory_Info = Car_inventory_Info('001', 'Ford', 'White', 'F', 'Stock', 'None')
json_string = json.dumps(car_inventory_Info, default=vars)
print(json_string)
response = chain.run(json_string)

# Car with ID 002 is a red BMW with all wheel drive. We currently have 6 in stock. Please provide the rim size for this car.
car_inventory_Info = Car_inventory_Info('002', 'BMW', 'Red', 'A', '6', 'rim')
json_string = json.dumps(car_inventory_Info, default=vars)
print(json_string)
response = chain.run(json_string)

# Car with ID 003 is a black Toyota with rear wheel drive. It is currently in transit and we need information about the car body.
car_inventory_Info = Car_inventory_Info('003', 'Toyota', 'Black', 'R', 'Transit', 'body')
json_string = json.dumps(car_inventory_Info, default=vars)
print(json_string)

response = chain.run(json_string)

print(response)
