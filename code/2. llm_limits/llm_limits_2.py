from ollama import chat

prompt = '''Escriba una sola línea del registro del servidor Apache que muestre una solicitud exitosa de un archivo estático. 
            Incluya solo el mensaje del registro, en una linea y sin comillas al principio'''


message = [
  {
    'role': 'user',
    'content': prompt,
  },
]

response = chat('llama3.2', messages=message)
print(response['message']['content'])