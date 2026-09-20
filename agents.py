from langchain.agents import create_agent
from llm import gemini_llm
from tools import live_cricket_score

gemini_agent = create_agent(
    model=gemini_llm,
    tools=[live_cricket_score],
    system_prompt="You are a helpful sport Assistant"
)

response = gemini_agent.invoke({"messages":{"role": "user", "content": "What is current cricket score between India  and pakistan"}})

print(response['messages'][-1].content[0]['text'])