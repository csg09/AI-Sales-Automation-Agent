"""
Automated Sales Development Representative (SDR)

This script implements a complete automated SDR system using:
- Multiple specialized sales agents
- Tool integration for email sending
- Agent handoffs for workflow delegation
- HTML email formatting with AI-generated subjects

This demonstrates advanced agentic patterns including planning,
tool use, and agent collaboration.
"""

import os
import asyncio
from typing import Dict
from dotenv import load_dotenv
import sendgrid
from sendgrid.helpers.mail import Mail, Email, To, Content
from agents import Agent, Runner, trace, function_tool


# Load environment variables
load_dotenv(override=True)


# ============================================================================
# AGENT INSTRUCTIONS
# ============================================================================

PROFESSIONAL_INSTRUCTIONS = """You are a sales agent working for ComplAI, \
a company that provides a SaaS tool for ensuring SOC2 compliance and preparing for audits, powered by AI. \
You write professional, serious cold emails."""

ENGAGING_INSTRUCTIONS = """You are a humorous, engaging sales agent working for ComplAI, \
a company that provides a SaaS tool for ensuring SOC2 compliance and preparing for audits, powered by AI. \
You write witty, engaging cold emails that are likely to get a response."""

CONCISE_INSTRUCTIONS = """You are a busy sales agent working for ComplAI, \
a company that provides a SaaS tool for ensuring SOC2 compliance and preparing for audits, powered by AI. \
You write concise, to the point cold emails."""

SUBJECT_INSTRUCTIONS = """You can write a subject for a cold sales email. \
You are given a message and you need to write a subject for an email that is likely to get a response."""

HTML_INSTRUCTIONS = """You can convert a text email body to an HTML email body. \
You are given a text email body which might have some markdown \
and you need to convert it to an HTML email body with simple, clear, compelling layout and design."""

EMAILER_INSTRUCTIONS = """You are an email formatter and sender. You receive the body of an email to be sent. \
You first use the subject_writer tool to write a subject for the email, then use the html_converter tool to convert the body to HTML. \
Finally, you use the send_html_email tool to send the email with the subject and HTML body."""

SALES_MANAGER_INSTRUCTIONS = """
You are a Sales Manager at ComplAI. Your goal is to find the single best cold sales email using the sales_agent tools.

Follow these steps carefully:
1. Generate Drafts: Use all three sales_agent tools to generate three different email drafts. Do not proceed until all three drafts are ready.

2. Evaluate and Select: Review the drafts and choose the single best email using your judgment of which one is most effective.
You can use the tools multiple times if you're not satisfied with the results from the first try.

3. Handoff for Sending: Pass ONLY the winning email draft to the 'Email Manager' agent. The Email Manager will take care of formatting and sending.

Crucial Rules:
- You must use the sales agent tools to generate the drafts — do not write them yourself.
- You must hand off exactly ONE email to the Email Manager — never more than one.
"""


# ============================================================================
# TOOLS - Function Decorators
# ============================================================================

@function_tool
def send_email(body: str) -> Dict[str, str]:
    """Send out an email with the given body to all sales prospects."""
    sender_email = os.environ.get('SENDER_EMAIL')
    recipient_email = os.environ.get('RECIPIENT_EMAIL')
    
    sg = sendgrid.SendGridAPIClient(api_key=os.environ.get('SENDGRID_API_KEY'))
    from_email = Email(sender_email)
    to_email = To(recipient_email)
    content = Content("text/plain", body)
    mail = Mail(from_email, to_email, "Sales email", content).get()
    sg.client.mail.send.post(request_body=mail)
    return {"status": "success"}


@function_tool
def send_html_email(subject: str, html_body: str) -> Dict[str, str]:
    """Send out an email with the given subject and HTML body to all sales prospects."""
    sender_email = os.environ.get('SENDER_EMAIL')
    recipient_email = os.environ.get('RECIPIENT_EMAIL')
    
    sg = sendgrid.SendGridAPIClient(api_key=os.environ.get('SENDGRID_API_KEY'))
    from_email = Email(sender_email)
    to_email = To(recipient_email)
    content = Content("text/html", html_body)
    mail = Mail(from_email, to_email, subject, content).get()
    sg.client.mail.send.post(request_body=mail)
    return {"status": "success"}


# ============================================================================
# AGENTS
# ============================================================================

# Sales Agents
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

# Email Formatting Agents
subject_writer = Agent(
    name="Email Subject Writer",
    instructions=SUBJECT_INSTRUCTIONS,
    model="gpt-4o-mini"
)

html_converter = Agent(
    name="HTML Email Body Converter",
    instructions=HTML_INSTRUCTIONS,
    model="gpt-4o-mini"
)


# ============================================================================
# CONVERT AGENTS TO TOOLS
# ============================================================================

# Sales agent tools
tool1 = sales_agent1.as_tool(
    tool_name="sales_agent1",
    tool_description="Write a cold sales email"
)

tool2 = sales_agent2.as_tool(
    tool_name="sales_agent2",
    tool_description="Write a cold sales email"
)

tool3 = sales_agent3.as_tool(
    tool_name="sales_agent3",
    tool_description="Write a cold sales email"
)

# Email formatting tools
subject_tool = subject_writer.as_tool(
    tool_name="subject_writer",
    tool_description="Write a subject for a cold sales email"
)

html_tool = html_converter.as_tool(
    tool_name="html_converter",
    tool_description="Convert a text email body to an HTML email body"
)


# ============================================================================
# EMAIL MANAGER AGENT (Handoff Target)
# ============================================================================

emailer_agent = Agent(
    name="Email Manager",
    instructions=EMAILER_INSTRUCTIONS,
    tools=[subject_tool, html_tool, send_html_email],
    model="gpt-4o-mini",
    handoff_description="Convert an email to HTML and send it"
)


# ============================================================================
# SALES MANAGER AGENT (Orchestrator)
# ============================================================================

sales_manager = Agent(
    name="Sales Manager",
    instructions=SALES_MANAGER_INSTRUCTIONS,
    tools=[tool1, tool2, tool3],
    handoffs=[emailer_agent],
    model="gpt-4o-mini"
)


# ============================================================================
# DEMONSTRATION FUNCTIONS
# ============================================================================

async def demo_basic_tool_usage():
    """Demonstrate basic tool usage with a simple sales manager."""
    print("=" * 60)
    print("Demo 1: Basic Tool Usage")
    print("=" * 60)
    print()
    
    basic_manager_instructions = """
You are a Sales Manager at ComplAI. Your goal is to find the single best cold sales email using the sales_agent tools.

Follow these steps carefully:
1. Generate Drafts: Use all three sales_agent tools to generate three different email drafts. Do not proceed until all three drafts are ready.

2. Evaluate and Select: Review the drafts and choose the single best email using your judgment of which one is most effective.

3. Use the send_email tool to send the best email (and only the best email) to the user.

Crucial Rules:
- You must use the sales agent tools to generate the drafts — do not write them yourself.
- You must send ONE email using the send_email tool — never more than one.
"""
    
    basic_manager = Agent(
        name="Basic Sales Manager",
        instructions=basic_manager_instructions,
        tools=[tool1, tool2, tool3, send_email],
        model="gpt-4o-mini"
    )
    
    message = "Send a cold sales email addressed to 'Dear CEO'"
    
    with trace("Basic Sales Manager"):
        result = await Runner.run(basic_manager, message)
    
    print("✅ Email sent using basic tool usage")
    print("ℹ️  Check the trace at: https://platform.openai.com/traces")
    print()


async def demo_full_sdr_system():
    """Demonstrate the full SDR system with handoffs and HTML formatting."""
    print("=" * 60)
    print("Demo 2: Full Automated SDR System")
    print("=" * 60)
    print()
    
    message = "Send out a cold sales email addressed to Dear CEO from Alice"
    
    with trace("Automated SDR"):
        result = await Runner.run(sales_manager, message)
    
    print("✅ HTML email sent using full SDR system")
    print("ℹ️  Check the trace at: https://platform.openai.com/traces")
    print("📧 Check your email inbox for the formatted message!")
    print()


async def main():
    """Run all demonstrations."""
    print("\n")
    print("*" * 60)
    print("AUTOMATED SDR SYSTEM")
    print("*" * 60)
    print("\n")
    
    # Verify environment variables
    if not os.environ.get('SENDGRID_API_KEY'):
        print("❌ Error: SENDGRID_API_KEY not found in .env file")
        return
    
    if not os.environ.get('SENDER_EMAIL'):
        print("❌ Error: SENDER_EMAIL not found in .env file")
        return
        
    if not os.environ.get('RECIPIENT_EMAIL'):
        print("❌ Error: RECIPIENT_EMAIL not found in .env file")
        return
    
    # Demo 1: Basic tool usage
    await demo_basic_tool_usage()
    
    # Demo 2: Full SDR system
    await demo_full_sdr_system()
    
    print("*" * 60)
    print("All demonstrations completed!")
    print("*" * 60)
    print("\n")
    print("Key Learnings:")
    print("- Tools: Agents and functions can be converted to tools")
    print("- Handoffs: Agents can delegate control to other agents")
    print("- Planning: Sales Manager orchestrates the entire workflow")
    print("- Observability: All actions are traced in OpenAI platform")
    print()


if __name__ == "__main__":
    asyncio.run(main())
