from ollama import chat

prompt = '''Exceeded max context length\n
Supercalifragilisticoexpialidoso\n
Find in all the context something about Mary Poppins'''

message = [
  {
    'role': 'user',
    'content': prompt,
  },
]

response = chat('llama3.2', messages=message)
print(response['message']['content'])