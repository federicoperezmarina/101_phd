import ollama

prompt = """
can you tell me which is your actual context window? please
"""


response_generate = ollama.generate(
  model='llama3.2',
  prompt=prompt,
  options={
    'num_ctx': 10000
  },
  keep_alive = "0"
)
print(response_generate['response'])