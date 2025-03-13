from ollama import chat

first_correct_log_message = "This is a correct log: 192.168.1.100 - - [12/Jul/2022:13:45:21 +0000] 'GET /path/to/static/file.css HTTP/1.1' 200 1027"
second_correct_log_message = "This is a correct log: 192.168.1.101 - - [12/Jul/2022:13:45:22 +0000] 'GET /path/to/static/file.js HTTP/1.1' 200 1248"
third_correct_log_message = "This is a correct log: 192.168.1.100 - - [12/Jul/2022:13:45:21 +0000] 'GET /path/to/static/design_system.css HTTP/1.1' 200 1038"

one_shot_prompts = [
    f""" ```{first_correct_log_message}```
    ```{second_correct_log_message}```
    ```{third_correct_log_message}```
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