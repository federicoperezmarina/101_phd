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
    'content': "The cafeteria had 23 apples. If they used 20 to make lunch and bought 6 more, how many apples do they have?"
  }  
]

response = chat('llama3.2', messages=messages)
print("Response output:")
for item in response:
    print(item)

print(response['message']['content'])