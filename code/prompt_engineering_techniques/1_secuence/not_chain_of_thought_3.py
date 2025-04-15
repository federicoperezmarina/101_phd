from ollama import chat

messages = [
  {
    'role': 'user',
    'content': ": John has 2 houses with 3 bedrooms each. Each bedroom has 2 windows each. There are an additional 4 windows in each house not connected to bedrooms. How many total windows are there between the houses?"
  }
]

response = chat('llama3.2', messages=messages)
print("Response output:")
for item in response:
    print(item)

print(response['message']['content'])