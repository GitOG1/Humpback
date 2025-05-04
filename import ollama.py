import ollama # type: ignore

desired_model = 'deepseek-r1:7b'  # Replace with your chosen model size
question_to_ask = 'How to solve a quadratic equation x^2+5*x+6=0'

response = ollama.chat(model=desired_model, messages=[
    {'role': 'user', 'content': question_to_ask},
])

ollama_response = response['message']['content']
print(ollama_response)

# Save the response to a file (optional)
with open("output_ollama.txt", "w") as f:
    f.write(ollama_response)
