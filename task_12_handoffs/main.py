# task 12: Handoffs in Agents
#  import necessary libraries
from agents import Agent, OpenAIChatCompletionsModel, Runner, set_tracing_disabled, handoff
from dotenv import load_dotenv
from openai import AsyncOpenAI
import os

load_dotenv(override=True)
set_tracing_disabled(True)

# get gemini API key and base URL from environment variables
gemini_api_key = os.getenv("GEMINI_API_KEY")
gemini_base_url = os.getenv("GEMINI_BASE_PATH")
gemini_model_name = os.getenv("GEMINI_MODEL_NAME")

client = AsyncOpenAI(api_key=gemini_api_key, base_url=gemini_base_url)
model = OpenAIChatCompletionsModel(openai_client=client, model=str(gemini_model_name))

# Lyrical Analysis Agent
lyrical_agent = Agent(
    name="Lyrical Agent",
    instructions="""
#   - You are a lyrical agent.
    - If the input is poetic or focuses on feelings and imagery, use the lyrical Agent.
    - explain the emotions,ideas it expresses.
    - Describe the message,theme it conveys.
    - Provide a clear and simple summary of its meaning.
    """,
    model=model,
)

# Narrative Analysis Agent
narrative_agent = Agent(
    name="Narrative Agent",
    instructions="""
    - You are a Narrative agent.
    - If the input tells a sequence of events or a story, use the narrative Agent.
    - explain the emotions,ideas it expresses.
    - Describe the message ,theme it conveys.
    - Provide a clear and simple summary of its meaning.
    """,
    model=model,
)

# Dramatic Analysis Agent
dramatic_agent = Agent(
    name="Dramatic Agent",
    instructions="""
    - You are a Dramatic agent.
    - If it is intense, suspenseful, or filled with strong emotions, use the Dramatic Agent.
    - explain the emotions,ideas it expresses.
    - Describe the message,theme it conveys.
    - Provide a clear and simple summary of its meaning.
    """,
    model=model,
)

# Triage Agent with handoffs
triage_agent = Agent(
    name="Triage Agent",
    instructions="""
    - You are a triage agent.
    - Your job is to analyze the given input and decide which agent is the best fit: Lyrical Agent, Narrative Agent, or Dramatic Agent. Based on your analysis, hand off the input to the selected agent. If the input is lyrical, narrative, or dramatic, you will call the respective agent to handle it.
    - define handoffs agnet name like hi i am then agnet name
    - then give the final output. 
    """,
    model=model,
    handoffs=[
        handoff(lyrical_agent),
        handoff(narrative_agent),
        handoff(dramatic_agent)
    ]
)

prompt = input("\n Enter the poem, story, or dramatic scene you want analyzed: ")
result = Runner.run_sync(triage_agent,prompt)
print("\nAnalysis Result:\n",result.final_output)