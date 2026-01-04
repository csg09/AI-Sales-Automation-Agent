"""
Basic Sales Agent Workflow

This script demonstrates the fundamental workflow of using multiple AI agents
to generate cold sales emails with different writing styles.

Features:
- Three agents with distinct personalities (professional, engaging, concise)
- Streaming output to see agent responses in real-time
- Parallel execution for efficiency
- AI-powered selection of the best email
"""

import os
import asyncio
from dotenv import load_dotenv
from agents import Agent, Runner, trace
from openai.types.responses import ResponseTextDeltaEvent


# Load environment variables
load_dotenv(override=True)


# Agent Instructions
PROFESSIONAL_INSTRUCTIONS = """You are a sales agent working for ComplAI, \
a company that provides a SaaS tool for ensuring SOC2 compliance and preparing for audits, powered by AI. \
You write professional, serious cold emails."""

ENGAGING_INSTRUCTIONS = """You are a humorous, engaging sales agent working for ComplAI, \
a company that provides a SaaS tool for ensuring SOC2 compliance and preparing for audits, powered by AI. \
You write witty, engaging cold emails that are likely to get a response."""

CONCISE_INSTRUCTIONS = """You are a busy sales agent working for ComplAI, \
a company that provides a SaaS tool for ensuring SOC2 compliance and preparing for audits, powered by AI. \
You write concise, to the point cold emails."""

SELECTOR_INSTRUCTIONS = """You pick the best cold sales email from the given options. \
Imagine you are a customer and pick the one you are most likely to respond to. \
Do not give an explanation; reply with the selected email only."""


# Initialize Agents
sales_agent1 = Agent(
    name="Professional Sales Agent",
    instructions=PROFESSIONAL_INSTRUCTIONS,
    model="gpt-4o-mini"
)

sales_agent2 = Agent(
    name="Engaging Sales Agent",
    instructions=ENGAGING_INSTRUCTIONS,
    model="gpt-4o-mini"
)

sales_agent3 = Agent(
    name="Concise Sales Agent",
    instructions=CONCISE_INSTRUCTIONS,
    model="gpt-4o-mini"
)

sales_picker = Agent(
    name="Email Selector",
    instructions=SELECTOR_INSTRUCTIONS,
    model="gpt-4o-mini"
)


async def demo_streaming_output():
    """Demonstrate streaming output from a single agent."""
    print("=" * 60)
    print("Demo 1: Streaming Output from Professional Agent")
    print("=" * 60)
    print()
    
    result = Runner.run_streamed(sales_agent1, input="Write a cold sales email")
    
    async for event in result.stream_events():
        if event.type == "raw_response_event" and isinstance(event.data, ResponseTextDeltaEvent):
            print(event.data.delta, end="", flush=True)
    
    print("\n")


async def demo_parallel_execution():
    """Demonstrate parallel execution of multiple agents."""
    print("=" * 60)
    print("Demo 2: Parallel Execution of Three Agents")
    print("=" * 60)
    print()
    
    message = "Write a cold sales email"
    
    with trace("Parallel Cold Emails"):
        results = await asyncio.gather(
            Runner.run(sales_agent1, message),
            Runner.run(sales_agent2, message),
            Runner.run(sales_agent3, message),
        )
    
    outputs = [result.final_output for result in results]
    
    print("Professional Agent Output:")
    print("-" * 60)
    print(outputs[0])
    print()
    
    print("Engaging Agent Output:")
    print("-" * 60)
    print(outputs[1])
    print()
    
    print("Concise Agent Output:")
    print("-" * 60)
    print(outputs[2])
    print("\n")


async def demo_ai_selection():
    """Demonstrate AI-powered selection of the best email."""
    print("=" * 60)
    print("Demo 3: AI-Powered Email Selection")
    print("=" * 60)
    print()
    
    message = "Write a cold sales email"
    
    with trace("Selection from Sales Agents"):
        # Generate emails in parallel
        results = await asyncio.gather(
            Runner.run(sales_agent1, message),
            Runner.run(sales_agent2, message),
            Runner.run(sales_agent3, message),
        )
        outputs = [result.final_output for result in results]
        
        # Format for selection
        emails = "Cold sales emails:\n\n" + "\n\nEmail:\n\n".join(outputs)
        
        # Select best email
        best = await Runner.run(sales_picker, emails)
        
        print("Best Sales Email Selected:")
        print("-" * 60)
        print(best.final_output)
        print()
    
    print("ℹ️  Check the trace at: https://platform.openai.com/traces")
    print()


async def main():
    """Run all demonstrations."""
    print("\n")
    print("*" * 60)
    print("AI SALES AGENT WORKFLOW DEMONSTRATIONS")
    print("*" * 60)
    print("\n")
    
    # Demo 1: Streaming
    await demo_streaming_output()
    
    # Demo 2: Parallel Execution
    await demo_parallel_execution()
    
    # Demo 3: AI Selection
    await demo_ai_selection()
    
    print("*" * 60)
    print("All demonstrations completed!")
    print("*" * 60)
    print()


if __name__ == "__main__":
    asyncio.run(main())
