from ollama import chat

messages = [
  {
    'role': 'user',
    'content': "Write a nginx log line. Only include the log message."
  },
]

response = chat('llama3.2', messages=messages)
print(response['message']['content'])