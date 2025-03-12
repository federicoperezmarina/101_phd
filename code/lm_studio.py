import lmstudio as lms

llm = lms.llm() # Get any loaded LLM

prediction = llm.respond_stream("What is a Capybara?")

for token in prediction:
    print(token, end="", flush=True)
