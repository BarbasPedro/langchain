from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate, ChatPromptTemplate
from langchain.chains import LLMChain, SimpleSequentialChain

import os
from dotenv import load_dotenv

llm = ChatOpenAI(
    model="gpt-3.5-turbo",
    temperature=0.5,
    api_key=os.getenv("OPENAI_API_KEY")
    )

load_dotenv()

prompt_cidade = ChatPromptTemplate(
    "Sugira uma cidade dado o meu interesse me {interesse}"
)

prompt_restaurantes = ChatPromptTemplate(
    "Sugira restaurantes populares entre locais em {cidade}"
)

prompt_cultural = ChatPromptTemplate(
    "Sugira atividades e locais culturais em {cidade}"
)

chain_cidade = LLMChain(prompt=prompt_cidade, llm=llm)
chain_restaurantes = LLMChain(prompt=prompt_restaurantes, llm=llm)
chain_cultural = LLMChain(prompt=prompt_cultural, llm=llm)

chain = SimpleSequentialChain(chains=[chain_cidade, chain_restaurantes, chain_cultural])

result = chain.invoke("praias")
print(result)