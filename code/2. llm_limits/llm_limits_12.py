import pandas as pd
from ollama import chat

# Read the dataset
df = pd.read_csv('dataset_dinosaurs.csv')

# Convert the dataframe to a string representation
context_prompt = df.to_string()

prompt = f'''Here is the dinosaur dataset:
{context_prompt}
Tell me the smallest dinosaur.'''

print(prompt)

message = [
    {
        'role': 'user',
        'content': prompt,
    },
]

response = chat('llama3.2', messages=message)
print(response['message']['content'])