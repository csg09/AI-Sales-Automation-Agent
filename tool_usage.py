"""
Tool Usage Examples

This script demonstrates various patterns for creating and using tools
with the OpenAI Agents SDK, including:
- Function tools with the @function_tool decorator
- Converting agents to tools
- Tool integration patterns
"""

import asyncio
from typing import Dict, List
from dotenv import load_dotenv
from agents import Agent, Runner, trace, function_tool


load_dotenv(override=True)


# ============================================================================
# EXAMPLE 1: Basic Function Tools
# ============================================================================

@function_tool
def calculate_roi(investment: float, return_amount: float) -> Dict[str, float]:
    """Calculate return on investment (ROI) percentage."""
    roi = ((return_amount - investment) / investment) * 100
    return {
        "investment": investment,
        "return": return_amount,
        "roi_percentage": round(roi, 2),
        "profit": round(return_amount - investment, 2)
    }


@function_tool
def get_company_info(company_name: str) -> Dict[str, str]:
    """Get mock company information (in production, this would query a real database)."""
    # Mock data for demonstration
    companies = {
        "acme": {
            "name": "Acme Corp",
            "industry": "Technology",
            "size": "500-1000 employees",
            "website": "acme.com"
        },
        "techstart": {
            "name": "TechStart Inc",
            "industry": "SaaS",
            "size": "50-100 employees",
            "website": "techstart.io"
        }
    }
    
    company_key = company_name.lower().replace(" ", "")
    return companies.get(company_key, {"error": "Company not found"})


@function_tool
def send_notification(message: str, priority: str = "normal") -> Dict[str, str]:
    """Send a notification (mock implementation)."""
    print(f"\n📢 [{priority.upper()}] Notification: {message}\n")
    return {"status": "sent", "priority": priority}


# ============================================================================
# EXAMPLE 2: Agents as Tools
# ============================================================================

research_agent = Agent(
    name="Research Assistant",
    instructions="You are a research assistant. Provide concise, factual information about topics.",
    model="gpt-4o-mini"
)

writer_agent = Agent(
    name="Content Writer",
    instructions="You are a content writer. Create engaging, well-structured content.",
    model="gpt-4o-mini"
)

# Convert agents to tools
research_tool = research_agent.as_tool(
    tool_name="research_assistant",
    tool_description="Research information about a topic"
)

writer_tool = writer_agent.as_tool(
    tool_name="content_writer",
    tool_description="Write content based on information"
)


# ============================================================================
# EXAMPLE 3: Agent with Multiple Tools
# ============================================================================

sales_analyzer = Agent(
    name="Sales Analyzer",
    instructions="""You are a sales analysis assistant. You can:
    - Calculate ROI for investments
    - Look up company information
    - Send notifications about important findings
    Use these tools to help analyze sales opportunities.""",
    tools=[calculate_roi, get_company_info, send_notification],
    model="gpt-4o-mini"
)


# ============================================================================
# DEMONSTRATION FUNCTIONS
# ============================================================================

async def demo_function_tools():
    """Demonstrate basic function tools."""
    print("=" * 60)
    print("Demo 1: Function Tools")
    print("=" * 60)
    print()
    
    with trace("Function Tools Demo"):
        result = await Runner.run(
            sales_analyzer,
            "Calculate the ROI if we invest $10,000 and get back $15,000. "
            "If the ROI is above 40%, send a high priority notification."
        )
    
    print(f"Result: {result.final_output}")
    print()


async def demo_agent_tools():
    """Demonstrate agents as tools."""
    print("=" * 60)
    print("Demo 2: Agents as Tools")
    print("=" * 60)
    print()
    
    coordinator = Agent(
        name="Content Coordinator",
        instructions="""You coordinate content creation. First use the research_assistant 
        to gather information, then use the content_writer to create engaging content 
        based on that research.""",
        tools=[research_tool, writer_tool],
        model="gpt-4o-mini"
    )
    
    with trace("Agent Tools Demo"):
        result = await Runner.run(
            coordinator,
            "Create a brief article about the benefits of AI in business"
        )
    
    print(f"Result: {result.final_output}")
    print()


async def demo_complex_workflow():
    """Demonstrate complex workflow with multiple tool types."""
    print("=" * 60)
    print("Demo 3: Complex Workflow")
    print("=" * 60)
    print()
    
    business_analyst = Agent(
        name="Business Analyst",
        instructions="""You are a business analyst. Analyze companies and opportunities.
        Look up company information, calculate potential ROI, and notify about good opportunities.
        A good opportunity has ROI > 30%.""",
        tools=[get_company_info, calculate_roi, send_notification],
        model="gpt-4o-mini"
    )
    
    with trace("Complex Workflow Demo"):
        result = await Runner.run(
            business_analyst,
            "Analyze TechStart as a potential client. Our service costs $50,000 "
            "and typically provides $80,000 in value. Should we pursue this opportunity?"
        )
    
    print(f"Result: {result.final_output}")
    print()


async def demo_tool_inspection():
    """Show how to inspect tool definitions."""
    print("=" * 60)
    print("Demo 4: Tool Inspection")
    print("=" * 60)
    print()
    
    print("Function Tool Definition:")
    print("-" * 60)
    print(f"Name: {calculate_roi.name}")
    print(f"Description: {calculate_roi.description}")
    print(f"Parameters: {calculate_roi.parameters}")
    print()
    
    print("Agent-as-Tool Definition:")
    print("-" * 60)
    print(f"Name: {research_tool.name}")
    print(f"Description: {research_tool.description}")
    print()


async def main():
    """Run all demonstrations."""
    print("\n")
    print("*" * 60)
    print("TOOL USAGE EXAMPLES")
    print("*" * 60)
    print("\n")
    
    await demo_tool_inspection()
    await demo_function_tools()
    await demo_agent_tools()
    await demo_complex_workflow()
    
    print("*" * 60)
    print("All examples completed!")
    print("*" * 60)
    print()
    print("Key Learnings:")
    print("- @function_tool decorator converts functions to tools")
    print("- agent.as_tool() converts agents to tools")
    print("- Tools enable agents to take actions and access data")
    print("- Multiple tools can be combined for complex workflows")
    print("\nCheck traces at: https://platform.openai.com/traces")
    print()


if __name__ == "__main__":
    asyncio.run(main())
