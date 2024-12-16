from openai import OpenAI
import os

from dotenv import load_dotenv, find_dotenv

_ = load_dotenv(find_dotenv())

client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

def get_completion(prompt, model='gpt-4o-mini'):
    messages = [{'role': 'user', 'content':prompt}]
    response = client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=0     
    )
    return response.choices[0].message.content

text= f"""
A synthesizer (also synthesiser or synth) is an electronic musical instrument that generates audio signals. Synthesizers typically create sounds by generating waveforms through methods including subtractive synthesis, additive synthesis and frequency modulation synthesis. These sounds may be altered by components such as filters, which cut or boost frequencies; envelopes, which control articulation, or how notes begin and end; and low-frequency oscillators, which modulate parameters such as pitch, volume, or filter characteristics affecting timbre. Synthesizers are typically played with keyboards or controlled by sequencers, software or other instruments, and may be synchronized to other equipment via MIDI.
"""
prompt = f"""
Summarize the text delimited by triple backticks into a single sentence.
```{text}```
"""

response = get_completion(prompt)
print(response)

