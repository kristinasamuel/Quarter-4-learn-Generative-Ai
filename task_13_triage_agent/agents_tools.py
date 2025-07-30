# task_13_triage_agent/agents_tools.py
from agents import Agent, function_tool

# Tools
@function_tool
def current_weather():
    print("📡 Weather tool called Successfully ")
    return "Currently 32°C and sunny in Karachi"

@function_tool
def get_latest_news():
    print("Get latest news tool called successfully")
    return "Latest news: The Ai industry is booming with new advancements every day."

# Sub-agents
plant_agent = Agent(
    name='Plant Agent',
    instructions="You are a plant expert agent.Your task is to Handle plant-related queries. ",
)

medicine_agent = Agent(
    name="Medicine Agent",
    instructions="You are a medicine expert.your task is to handle medicine-related queries.",
)

# Parent agent
triage_agent = Agent(
    name="Triage Agent",
    instructions="""
        You are the triage agent. Route the user queries to the correct sub-agent or tool.
       - If the user asks about current location or weather, use the available tools.
       - If the user asks about plants, forward the query to `plant_agent`.
       - If the user asks about medicine, forward the query to `medicine_agent`.
       - If the user asks anything unrelated, respond: Sorry, I can't help with that request.
    """,
    handoffs=[plant_agent, medicine_agent],
    tools=[current_weather, get_latest_news]
)
