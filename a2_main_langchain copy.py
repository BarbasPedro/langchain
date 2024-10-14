from langchain_openai import ChatOpenAI
import os
from dotenv import load_dotenv

load_dotenv()

numero_de_pessoas = 4
numero_de_criancas = 2
atividade = 'praia'

prompt = f"Crie um roteiro de viagem de {numero_de_pessoas}, onde {numero_de_criancas} são crianças que gostam de {atividade}"

llm = ChatOpenAI(
    model="gpt-3.5-turbo",
    temperature=0.5,
    api_key="OPENAI_API_KEY"
    )

res = llm.invoke(prompt)
print(res.content)