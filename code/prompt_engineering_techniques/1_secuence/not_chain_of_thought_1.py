from ollama import chat

messages = [
  {
    'role': 'user',
    'content': "The cafeteria had 23 apples. If they used 20 to make lunch and bought 6 more, how many apples do they have?"
  }  
]

response = chat('llama3.2', messages=messages)
print("Response output:")
for item in response:
    print(item)

print(response['message']['content'])