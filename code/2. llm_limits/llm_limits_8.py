from ollama import chat

context_prompt = "Este es un texto de prueba. \n" * 1000000

prompt = 'Supercalifragilisticoexpialidoso \n'+context_prompt+'''\nFind in all the context something about Mary Poppins'''

# Save the prompt to a file
with open('book_created.txt', 'w') as file:
    file.write(prompt)


message = [
  {
    'role': 'user',
    'content': prompt,
  },
]

response = chat('llama3.2', messages=message)
print(response['message']['content'])