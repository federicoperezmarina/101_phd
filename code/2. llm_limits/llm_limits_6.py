from ollama import chat

# Read the context from file
with open('book_pride_and_prejudice.txt', 'r') as file:
    context_prompt = file.read()

prompt = 'Supercalifragilisticoexpialidoso \n'+context_prompt+'''\nFind in all the context something about Mary Poppins'''

message = [
  {
    'role': 'user',
    'content': prompt,
  },
]

response = chat('llama3.2', messages=message)
print(response['message']['content'])