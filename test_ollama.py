from ollama import chat
resp = chat(
  model='llama3',  # or the exact tag from `ollama list`, e.g., 'llama3.2:3b'
  messages=[{'role':'user','content':'Write a short poem about AI.'}]
)
print(resp['message']['content'])
