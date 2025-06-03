from ollama import chat

prompt = """
Eres un asistente generador de JSON especializado en datos de Dragon Ball. Validaremos la información con https://dragonball-api.com/

Razonemos paso a paso.

Vamos a crear una matriz JSON que incluya información sobre personajes conocidos del universo Dragon Ball.

Paso 1: Piensa en al menos 10 personajes populares. Sugerencias: Goku, Vegeta, Piccolo, Gohan, Freezer.

Paso 2: Para cada personaje, recopila los siguientes atributos:
- id: un identificador secuencial único del personaje
- name: el nombre del personaje
- power_level_ki: nivel de poder numérico estimado - ki (sin comillas)
- max_power_level_ki: nivel de poder numérico máximo estimado (sin comillas)
- race: su especie (p. ej., Saiyan, Namek)
- gender: su género (masculino, femenino u otro)
- description: una breve descripción del personaje
- image_url: una URL a una imagen del personaje
- origin_planet: su planeta de origen

Paso 3: Organiza los datos en una matriz JSON limpia. Cada personaje debe ser un objeto independiente con todos los campos incluidos.

Imprime solo el JSON final. No incluyas explicaciones ni razonamientos en la salida.
"""


message = [
  {
    'role': 'user',
    'content': prompt,
  },
]

response = chat('llama3.2', messages=message)
print(response['message']['content'])