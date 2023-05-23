import os
import openai
import requests as req
from flask import Flask
from web3 import Web3
import langchain

from src.agent import Agent

app = Flask(__name__)

openai.api_key = os.getenv("OPENAI_API_KEY")
openai.organization = os.getenv("OPENAI_ORG")

# @app.route("/")
# def create():
#     return "API v0.0"

# if __name__== '__main__':
#     app.run(debug=True)
system_msg = "You are a friendly assistant that wants to help humans with any questions that they may have. You want to provide information as accurately as possible and as without bias as much as possible, attempting to present both sides when they're relevant to being presented. You will try to demonstrate and illustrate complex concepts with analogies and input any well known tips and tricks when relevant."
prompt = "Can you help me create a an outline for a content creation business. I would like you to ask me a list of 20+ questions, to create a growing, successful business. The content the business will generally revolve around is geopolitics and finance. In particular, political events and finance from a leftist/socialist perspective."

agent = Agent(openai.api_key, "gpt-3.5-turbo-0301", verbose=True)
agent.initialise(system_msg)
response = agent.open_interaction(prompt)
print(response)

# agent.complete(prompt)


