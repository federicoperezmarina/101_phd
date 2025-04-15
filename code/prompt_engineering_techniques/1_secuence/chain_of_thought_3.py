from ollama import chat

messages = [
  {
    'role': 'user',
    'content': "Roger has 5 tennis balls. He buys 2 more cans of tennis balls. Each can has 3 tennis balls. How many tennis balls does he have now?"
  },
  {
    'role': 'assistant',
    'content': "Roger started with 5 balls. 2 cans of 3 tennis balls each is 6 tennis balls. 5 + 6 = 11. The answer is 11."
  },  
  {
    'role': 'user',
    'content': "John has 2 houses with 3 bedrooms each. Each bedroom has 2 windows each. There are an additional 4 windows in each house not connected to bedrooms. How many total windows are there between the houses?"
  },  
]

response = chat('llama3.2', messages=messages)
print("Response output:")
for item in response:
    print(item)

print(response['message']['content'])