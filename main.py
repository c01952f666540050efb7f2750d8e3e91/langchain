import os
import openai
import requests as req

openai.organization = "org-4E7mUR9VSwp5bzxHJB2BkXIW"
openai.api_key = os.getenv("OPENAI_API_KEY")

# prompt = "How can I create an ERC20 token in solidity?"
response = openai.ChatCompletion.create(model="gpt-3.5-turbo",messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": "How can I create an ERC20 token in solidity?"}
        ]
        , temperature=0)
print(response)