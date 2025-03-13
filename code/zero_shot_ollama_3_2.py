from ollama import chat

zero_shot_prompts = [
    "Write a single line from the Apache server log showing a successful request for a static file. Only include the log message.",
    "Create a line from the Apache server log indicating a failed authentication attempt for a user trying to access a protected resource. Only include the log message.",
    "Generate a line from the Apache server log detailing the completion of a long-running database query. Only include the log message.",
    "Write a single line from the Apache server log showing an error 500 response due to a configuration issue. Only include the log message.",
    "Create a line from the Apache server log indicating the successful delivery of an email via a third-party service. Only include the log message.",
    "Generate a line from the Apache server log detailing the request for a favicon icon by a browser. Only include the log message.",
    "Write a single line from the Apache server log showing an idle connection to the server that has been inactive for more than 30 minutes. Only include the log message.",
    "Create a line from the Apache server log indicating a successful download of a file via HTTPRangeRequest. Only include the log message.",
    "Generate a line from the Apache server log detailing the request for an SSL/TLS certificate by a client browser. Only include the log message.",
    "Write a single line from the Apache server log showing an error 502 response due to a timeout issue while connecting to a remote resource. Only include the log message."
]

for prompt in zero_shot_prompts:
    messages = [
      {
        'role': 'user',
        'content': prompt,
      },
    ]

    response = chat('llama3.2', messages=messages)
    print(response['message']['content'])