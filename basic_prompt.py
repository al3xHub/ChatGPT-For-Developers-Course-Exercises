from openai import OpenAI
import os
from dotenv import load_dotenv, find_dotenv

_ = load_dotenv(find_dotenv())

client=OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

completion = client.chat.completions.create(
    model='gpt-4o-mini',
    messages=[
        {'role':'system', 'content': 'You are a helpful assistant'},
        {'role':'user', 'content': 'tell me a joke about cats'}
    ]
)

print(completion.choices[0].message)