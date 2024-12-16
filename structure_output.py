from openai import OpenAI
import os
from dotenv import load_dotenv, find_dotenv

_ = load_dotenv(find_dotenv())

client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

def get_completion(prompt, model='gpt-4o-mini'):
    messages = [{'role':'user', 'content':prompt}]
    response = client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=0   
    )
    return response.choices[0].message.content

prompt = f"""
Generate a list of three made-up book titles along \ 
with their authors and genres. 
Provide them in JSON format with the following keys: 
book_id, title, author, genre.
"""
response = get_completion(prompt)
print(response)