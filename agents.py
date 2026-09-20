from langchain.agents import create_agent
from llm import gemini_llm
from tools import live_cricket_score
from langgraph.checkpoint.memory import InMemorySaver

gemini_agent = create_agent(
    model=gemini_llm,
    tools=[live_cricket_score],
    system_prompt="You are a helpful sport Assistant",
    checkpointer= InMemorySaver()
)

