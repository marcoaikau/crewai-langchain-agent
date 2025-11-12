from crewai import Agent, Crew
from langchain.llms import OpenAI
import os

os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

llm = OpenAI(temperature=0.3, model="gpt-4o-mini")

agente = Agent(
    role="Assistente",
    goal="Responder perguntas do usuário",
    backstory="Você é um assistente prestativo e direto."
)

crew = Crew(agents=[agente])

resultado = crew.kickoff(goal="Explique o que são closures em JavaScript.")
print(resultado)
