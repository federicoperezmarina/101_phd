from ollama import chat

prompt = '''Scribere unam lineam Apache servo stipes ostendens feliciter petitionem statice lima. 
            Solum nuntium truncum in una linea et sine initio includunt.'''


message = [
  {
    'role': 'user',
    'content': prompt,
  },
]

response = chat('llama3.2', messages=message)
print(response['message']['content'])