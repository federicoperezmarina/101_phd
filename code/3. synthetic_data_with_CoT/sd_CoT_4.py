import ollama

prompt = """
Eres un asistente generador de JSON especializado en datos de Dragon Ball. 

Razonemos paso a paso.

Vamos a crear una matriz JSON que incluya información sobre personajes conocidos del universo Dragon Ball.

Paso 1: Piensa en 10 personajes populares. Sugerencias: Goku, Vegeta.

Paso 2: Para cada personaje, recopila los siguientes atributos:
- id: un identificador secuencial único del personaje
- name: el nombre del personaje
- power_level_ki: nivel de poder numérico estimado 
- max_power_level_ki: nivel de poder numérico máximo estimado
- race: su especie debe estar dentro de las siguientes razas, Saiyan, Namekian, Human, Majin, Frieza Race, Jiren Race, Android, God, Angel, Evil, Unknown, Nucleico benigno, Nucleico
- gender: su género (Masculino, Femenino, Otros, Desconocido)
- description: una breve descripción del personaje
- image_url: una url de imagen valida del personaje que se pueda visualizar en el navegador. Debe seguir este formato: https://dragonball-api.com/characters/{name}.webp

Paso 3: Organiza los datos en una matriz JSON limpia. clearCada personaje debe ser un objeto independiente con todos los campos id, name, power_level_ki, max_power_level_ki, race, gender, description, image_url.

Imprime solo el JSON final. No incluyas explicaciones ni razonamientos en la salida.
"""


response_generate = ollama.generate(
  model='llama3.2',
  prompt=prompt,
#  options={
#    'num_ctx': 7500
#  }
)

print(response_generate['response'])