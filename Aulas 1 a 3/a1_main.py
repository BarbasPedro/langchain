from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

numero_de_pessoas = 4
atividade = 'praia'

prompt = f"Crie um roteiro de viagem de {numero_de_pessoas} que gostam de {atividade}"
print(prompt)

cliente = OpenAI(api_key="OPENAI_API_KEY")

resposta = cliente.chat.completions.create(
    model="gpt-3.5-turbo",
    messages = [
        {"role": "system", "content": "You are a helpful assistance"},
        {"role": "user", "content": prompt }
    ],
)

# print(resposta)
roteiro = resposta.choices[0].message.content
print(roteiro)