from ollama import chat

prompt = """
Let's think step by step.

I want to create a JSON file containing information about characters from the Dragon Ball universe.

First, I will list the characters. Let's include well-known characters like Goku, Vegeta, Piccolo, Gohan, Trunks, and Frieza.

Second, for each character, I need to gather specific attributes:
- full_name: the complete name of the character
- race: the species or race (e.g., Saiyan, Namekian, Human)
- power_level: a numeric estimation of their maximum power level
- height_cm: height in centimeters
- weight_kg: weight in kilograms
- role: their general alignment or role (e.g., Hero, Villain, Anti-hero)

Now, I will organize this information into a well-formatted JSON array. Each character will be an object in the array, using the keys mentioned above.

Output only the final JSON content, nothing else.
"""


message = [
  {
    'role': 'user',
    'content': prompt,
  },
]

response = chat('llama3.2', messages=message)
print(response['message']['content'])