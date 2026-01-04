"""
Parallel Agent Execution Example

This example demonstrates how to run multiple agents concurrently
using asyncio.gather() for improved performance.
"""

import asyncio
from dotenv import load_dotenv
from agents import Agent, Runner, trace


load_dotenv(override=True)


# Define different agent personalities
agents_config = [
    {
        "name": "Professional Writer",
        "instructions": "You write in a formal, professional tone. Keep responses clear and structured.",
    },
    {
        "name": "Creative Writer",
        "instructions": "You write in a creative, engaging tone with metaphors and storytelling.",
    },
    {
        "name": "Technical Writer",
        "instructions": "You write in a technical, precise tone with specific details and terminology.",
    },
]


async def run_parallel_agents():
    """Execute multiple agents in parallel and compare outputs."""
    
    # Create agents
    agents = [
        Agent(
            name=config["name"],
            instructions=config["instructions"],
            model="gpt-4o-mini"
        )
        for config in agents_config
    ]
    
    # Task for all agents
    task = "Explain what artificial intelligence is in 3 sentences."
    
    print("Running agents in parallel...")
    print(f"Task: {task}\n")
    
    # Execute in parallel with tracing
    with trace("Parallel Agent Execution"):
        results = await asyncio.gather(
            *[Runner.run(agent, task) for agent in agents]
        )
    
    # Display results
    for i, result in enumerate(results):
        print(f"\n{'='*60}")
        print(f"{agents_config[i]['name']} Output:")
        print(f"{'='*60}")
        print(result.final_output)
    
    print(f"\n{'='*60}")
    print("All agents completed!")
    print("Check trace at: https://platform.openai.com/traces")


async def measure_performance():
    """Compare parallel vs sequential execution time."""
    import time
    
    agents = [
        Agent(
            name=config["name"],
            instructions=config["instructions"],
            model="gpt-4o-mini"
        )
        for config in agents_config
    ]
    
    task = "Write a one-sentence product description for AI software."
    
    # Sequential execution
    print("\nTesting Sequential Execution...")
    start = time.time()
    for agent in agents:
        await Runner.run(agent, task)
    sequential_time = time.time() - start
    
    # Parallel execution
    print("Testing Parallel Execution...")
    start = time.time()
    await asyncio.gather(
        *[Runner.run(agent, task) for agent in agents]
    )
    parallel_time = time.time() - start
    
    # Results
    print(f"\n{'='*60}")
    print("Performance Comparison:")
    print(f"{'='*60}")
    print(f"Sequential: {sequential_time:.2f} seconds")
    print(f"Parallel:   {parallel_time:.2f} seconds")
    print(f"Speedup:    {sequential_time/parallel_time:.2f}x faster")


async def main():
    """Run all demonstrations."""
    print("\n" + "="*60)
    print("PARALLEL AGENT EXECUTION EXAMPLES")
    print("="*60 + "\n")
    
    await run_parallel_agents()
    await measure_performance()
    
    print("\n" + "="*60)
    print("Examples completed!")
    print("="*60 + "\n")


if __name__ == "__main__":
    asyncio.run(main())
