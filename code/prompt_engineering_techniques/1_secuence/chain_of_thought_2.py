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
    'content': "There are 36 penguins sunbathing in the snow. One-third of them jump in and swim in the ocean. Another one-third go inside the cave to eat their dinner. How many penguins are still left sunbathing?"
  }
]

response = chat('llama3.2', messages=messages)
print("Response output:")
for item in response:
    print(item)

print(response['message']['content'])