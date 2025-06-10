import os
import json
from dotenv import load_dotenv
from openai import OpenAI
from IPython.display import display


load_dotenv(override=True)
openai_api_key = os.getenv('OPENAI_API_KEY')

openai = OpenAI()  # Initialize the OpenAI client

request = "Please come up with a challenging, nuanced question that I can ask a number of LLMs to evaluate their intelligence. "
request += "Answer only with the question, no explanation."
messages = [{"role": "user", "content": request}]

response = openai.chat.completions.create(  
    model="gpt-4.1-mini",
    messages=messages
)

question = response.choices[0].message.content

response = openai.chat.completions.create(
    model="gpt-4.1-mini",
    messages=[{"role": "user", "content": question}]
)

answer = response.choices[0].message.content

print(question)
display((answer))
