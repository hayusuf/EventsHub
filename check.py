import os
import openai
openai.api_type = "azure"
openai.api_base = 'https://api.umgpt.umich.edu/azure-openai-api/ptu'
openai.api_key="b5dd31fb62e843569434325e2664cd3d"
openai.api_version="2023-07-01-preview"

response = openai.ChatCompletion.create(
    engine="gpt-4", # engine = "deployment_name".
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Does Azure OpenAI support customer managed keys?"},
        {"role": "assistant", "content": "Yes, customer managed keys are supported by Azure OpenAI."},
        {"role": "user", "content": "Do other Azure AI services support this too?"}
    ]
)
print(response['choices'][0]['message']['content'])