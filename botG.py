from langchain.llms.google_palm import GooglePalm
from langchain.agents import AgentType, initialize_agent, load_tools
from apis import SERPAPI_API_KEY, GOOGLE_API_KEY
import os

os.environ['SERPAPI_API_KEY'] = SERPAPI_API_KEY
os.environ['GOOGLE_API_KEY'] = GOOGLE_API_KEY

llm = GooglePalm(temperature=0.1)
tools = load_tools(['serpapi'], llm=llm)
agent = initialize_agent(tools, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True)

def query(question):
    return agent.run(question)