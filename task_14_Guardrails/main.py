import asyncio
from pydantic import BaseModel
from config import config
from agents import (
    Agent,
    Runner,
    input_guardrail,
    GuardrailFunctionOutput,
    InputGuardrailTripwireTriggered,
    trace
)

# Output Model
class ChangeClassTiming(BaseModel):
    response: str
    isTimeChangeRequested: bool

# Admin Agent

admin_agent = Agent(
    name="Admin Agent",
    instructions="""
       You are an admin agent. Your job is to listen to queries from students and teachers. 
       If someone asks to change the class timing, politely say that it cannot be changed.
    """,
    output_type=ChangeClassTiming,
)

# Input Guardrail Function
@input_guardrail
async def admin_guardrail(ctx, agent: Agent, input: str) -> GuardrailFunctionOutput:
    result = await Runner.run(admin_agent, input, run_config=config, context=ctx)
    print("🛡️ Admin Agent Decision:")
    print(result.final_output)

    return GuardrailFunctionOutput(
        output_info=result.final_output,
        tripwire_triggered=result.final_output.isTimeChangeRequested
    )

# Teacher Agent
teacher_agent = Agent(
    name="Teacher Agent",
    instructions="""
       You are a strict teacher who answers student queries. 
       All student inputs are first checked by the Admin Agent.
    """,
    input_guardrails=[admin_guardrail]
)

# ✅ Main Runner with Tracing
async def main():
    try:
        user_input = "I want to change my class timing" 
        with trace("Input Guardrail"):
            result = await Runner.run(
                teacher_agent,
                user_input,
                run_config=config
            )
            print("🟢 Final Output:", result.final_output)
    except InputGuardrailTripwireTriggered:
        print("🚫 Unfortunately, class timings cannot be adjusted. Please follow the current schedule.")

if __name__ == "__main__":
    asyncio.run(main())
