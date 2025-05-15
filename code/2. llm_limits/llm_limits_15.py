import pandas as pd
from ollama import chat
from typing import List, Dict
from dataclasses import dataclass
import json

@dataclass
class DragonBallCharacter:
    name: str
    race: str
    power_level: int
    height:int
    weight:int
    role: str

def read_dragon_ball_characters() -> List[DragonBallCharacter]:
    df = pd.read_csv('dataset_dragon_ball.csv')
    characters = []
    
    for _, row in df.iterrows():
        character = DragonBallCharacter(
            name=row['Personaje'],
            race=row['Raza'],
            power_level=int(row['Nivel de Poder']),
            height=row['Altura (m)'],
            weight=row['Peso (kg)'],
            role=row['Personalidad / Rol Principal']
        )
        characters.append(character)
    
    return characters

# Read and structure the data
characters = read_dragon_ball_characters()

# Convert to a more readable format for the LLM
structured_data = [
    {
        "name": c.name,
        "race": c.race,
        "power_level": c.power_level,
        "height":c.height,
        "weight":c.weight,
        "role": c.role
    }
    for c in characters
]

# Create a prompt with the structured data
prompt = f'''Here is a structured dataset of Dragon Ball characters:
{json.dumps(structured_data, indent=2)}
Dime cual es el personaje más bajo la salida tiene que ser solo nombre:altura, si hay mas de uno indícamelo.'''

print(prompt)

message = [
    {
        'role': 'user',
        'content': prompt,
    },
]

response = chat('llama3.2', messages=message)
print(response['message']['content'])