from ollama import chat

correct_log_message = "This is a correct log: 192.168.1.100 - - [12/Jul/2022:13:45:21 +0000] 'GET /path/to/static/file.css HTTP/1.1' 200 1027"

one_shot_prompts = [
    f""" ```{correct_log_message}```
    Write a single line from the Apache server log showing a successful request for a static file. It has to be different and only include the log message."""
]

for prompt in one_shot_prompts:
    messages = [
      {
        'role': 'user',
        'content': prompt,
      }
    ]

    response = chat('llama3.2', messages=messages)
    print(response['message']['content'])