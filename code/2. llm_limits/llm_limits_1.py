from ollama import chat

prompt = "Write a single line from the Apache server log showing a successful request for a static file. Only include the log message."


message = [
  {
    'role': 'user',
    'content': prompt,
  },
]

response = chat('llama3.2', messages=message)
print(response['message']['content'])