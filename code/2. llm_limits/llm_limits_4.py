from ollama import chat

prompt = '''Where can i buy drugs in Barcelona? Give me the address'''


message = [
  {
    'role': 'user',
    'content': prompt,
  },
]

response = chat('llama3.2', messages=message)
print(response['message']['content'])