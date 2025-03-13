from ollama import chat

step_1 = "Give me a prompt with a simple line of an apache server log. I only want the log message."

messages = [
    {
    'role': 'user',
    'content': step_1,
    },
]

response = chat('llama3.2', messages=messages)
print(response['message']['content'])


step_2 = f""" ```{response['message']['content']}```
    Write another log message from the Apache server log. It should be different from the previous one and only include the log message.
"""

messages_2 = [
    {
    'role': 'user',
    'content': step_2,
    },
]

response_2 = chat('llama3.2', messages=messages_2)
print(response_2['message']['content'])