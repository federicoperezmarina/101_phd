from ollama import chat

#Prompt for math word problems - chain of thought
messages = [
  {
    'role': 'user',
    'content': "There are 15 trees in the grove. Grove workers will plant trees in the grove today. After they are done, there will be 21 trees. How many trees did the grove workers plant today?"
  },
  {
    'role': 'assistant',
    'content': "here are 15 trees originally. Then there were 21 trees after some more were planted. So there must have been 21 - 15 = 6. The answer is 6."
  },  
  {
    'role': 'user',
    'content': "If there are 3 cars in the parking lot and 2 more cars arrive, how many cars are in the parking lot?"
  },
  {
    'role': 'assistant',
    'content': "There are originally 3 cars. 2 more cars arrive. 3 + 2 = 5. The answer is 5."
  },    
  {
    'role': 'user',
    'content': "Leah had 32 chocolates and her sister had 42. If they ate 35, how many pieces do they have left in total?"
  },
  {
    'role': 'assistant',
    'content': "Originally, Leah had 32 chocolates. Her sister had 42. So in total they had 32 + 42 = 74. After eating 35, they had 74 - 35 = 39. The answer is 39."
  },   
  {
    'role': 'user',
    'content': "Jason had 20 lollipops. He gave Denny some lollipops. Now Jason has 12 lollipops. How many lollipops did Jason give to Denny?"
  },
  {
    'role': 'assistant',
    'content': "Jason started with 20 lollipops. Then he had 12 after giving some to Denny. So he gave Denny 20 - 12 = 8. The answer is 8."
  },   
  {
    'role': 'user',
    'content': "Shawn has five toys. For Christmas, he got two toys each from his mom and dad. How many toys does he have now?"
  },
  {
    'role': 'assistant',
    'content': "Shawn started with 5 toys. If he got 2 toys each from his mom and dad, then that is 4 more toys. 5 + 4 = 9. The answer is 9."
  },   
  {
    'role': 'user',
    'content': "There were nine computers in the server room. Five more computers were installed each day, from monday to thursday. How many computers are now in the server room?"
  },
  {
    'role': 'assistant',
    'content': "There were originally 9 computers. For each of 4 days, 5 more computers were added. So 5 * 4 = 20 computers were added. 9 + 20 is 29. The answer is 29."
  },   
  {
    'role': 'user',
    'content': "Michael had 58 golf balls. On tuesday, he lost 23 golf balls. On wednesday, he lost 2 more. How many golf balls did he have at the end of wednesday?"
  },
  {
    'role': 'assistant',
    'content': "Michael started with 58 golf balls. After losing 23 on tuesday, he had 58 - 23 = 35. After losing 2 more, he had 35 - 2 = 33 golf balls. The answer is 33."
  },   
  {
    'role': 'user',
    'content': "Olivia has $23. She bought five bagels for $3 each. How much money does she have left?"
  },
  {
    'role': 'assistant',
    'content': "Olivia had 23 dollars. 5 bagels for 3 dollars each will be 5 x 3 = 15 dollars. So she has 23 - 15 dollars left. 23 - 15 is 8. The answer is 8."
  }
]

messages.append({
    'role': 'user',
    'content': "John has 2 houses with 3 bedrooms each. Each bedroom has 2 windows each. There are an additional 4 windows in each house not connected to bedrooms. How many total windows are there between the houses?"
  })

response = chat('llama3.2', messages=messages)
print("Response output:")
for item in response:
    print(item)

print(response['message']['content'])