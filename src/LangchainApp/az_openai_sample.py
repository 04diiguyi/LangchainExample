from api_key import Az_OpenAI_api_key, Az_OpenAO_endpoint, Az_Open_Deployment_name

import openai

openai.api_key = Az_OpenAI_api_key
openai.api_base = Az_OpenAO_endpoint
openai.api_type = 'azure'
openai.api_version = '2023-05-15'

deployment_name=Az_Open_Deployment_name

# Send a completion call to generate an answer
print('Sending a test completion job')
start_phrase = 'Write a tagline for an ice cream shop. '
response = openai.Completion.create(engine=deployment_name, prompt=start_phrase, max_tokens=10)
text = response['choices'][0]['text'].replace('\n', '').replace(' .', '.').strip()
print(start_phrase+text)

print(text)