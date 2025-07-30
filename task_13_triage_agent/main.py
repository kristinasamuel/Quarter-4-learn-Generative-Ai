# main.py
import asyncio
from agents import Runner, trace
from config import config
from agents_tools import triage_agent

async def main():
    user_input = input("💬 Enter your question: ")
    with trace("trace User Prompt"):
        # Run the triage agent with the user input
        result = await Runner.run(
            triage_agent,
            user_input,
            run_config=config
        )
        print("🟢 Final Output :", result.final_output)
        print("🔚 Last Agent:", result.last_agent.name)

if __name__ == "__main__":
    asyncio.run(main())