from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
import os
from dotenv import load_dotenv

load_dotenv()

numero_de_pessoas = 4
numero_de_criancas = 2
atividade = 'praia'

template = PromptTemplate.from_template(
    "Crie um roteiro de viagem de {pessoas}, onde {criancas} são crianças que gostam de {atv}"
)

prompt = template.format(
    pessoas=numero_de_pessoas,
    criancas=numero_de_criancas,
    atv=atividade
)

llm = ChatOpenAI(
    model="gpt-3.5-turbo",
    temperature=0.5,
    api_key=os.getenv("OPENAI_API_KEY")
    )

res = llm.invoke(prompt)
print(res.content)