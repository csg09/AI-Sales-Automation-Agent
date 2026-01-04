# Quick Start Guide

Get up and running with the AI Sales Automation Agent in 5 minutes.

## Prerequisites

- Python 3.8 or higher
- OpenAI API key
- SendGrid account (free tier works)

## Step 1: Clone and Install

```bash
# Clone the repository
git clone https://github.com/csg09/ai-sales-automation-agent.git
cd ai-sales-automation-agent

# Install dependencies
pip install -r requirements.txt
```

## Step 2: Configure Environment

```bash
# Copy environment template
cp .env.example .env
```

Edit `.env` and add your credentials:

```env
OPENAI_API_KEY=sk-...your-key-here...
SENDGRID_API_KEY=SG....your-key-here...
SENDER_EMAIL=your-verified-email@example.com
RECIPIENT_EMAIL=recipient@example.com
```

### Getting Your API Keys

**OpenAI API Key:**
1. Visit https://platform.openai.com/api-keys
2. Click "Create new secret key"
3. Copy the key to your `.env` file

**SendGrid API Key:**
1. Sign up at https://sendgrid.com/ (free)
2. Go to Settings → API Keys → Create API Key
3. Copy the key to your `.env` file
4. **Important**: Verify your sender email at Settings → Sender Authentication

## Step 3: Test Configuration

```bash
# Test email configuration
python test_email.py
```

You should see:
```
✅ Success! Test email sent successfully.
   Status Code: 202
```

Check your email inbox (and spam folder) for the test message.

## Step 4: Run Examples

### Basic Sales Agent Workflow

```bash
python basic_sales_agent.py
```

This demonstrates:
- Streaming output from agents
- Parallel execution of multiple agents
- AI-powered email selection

### Full Automated SDR System

```bash
python automated_sdr.py
```

This demonstrates:
- Complete SDR workflow
- Tool integration (function calling)
- Agent handoffs
- HTML email formatting

## Step 5: View Traces

All agent executions are traced. View them at:

https://platform.openai.com/traces

Traces show you:
- Agent decision-making process
- Tool calls and responses
- Handoff transitions
- Performance metrics

## Next Steps

### Explore Examples

Check out the `examples/` directory:

```bash
# Parallel execution patterns
python examples/parallel_execution.py

# Tool usage patterns
python examples/tool_usage.py
```

### Customize Agents

Edit the agent instructions in the Python files to:
- Change writing styles
- Add new agent personalities
- Modify the sales pitch
- Adjust selection criteria

### Integrate with Your System

The code is designed to be modular. You can:
- Replace SendGrid with your email provider
- Add your own tools and functions
- Integrate with CRM systems
- Add database lookups
- Implement webhook handlers

## Troubleshooting

### SSL Certificate Errors

```bash
pip install --upgrade certifi
```

Then add to your script:
```python
import certifi
import os
os.environ['SSL_CERT_FILE'] = certifi.where()
```

### Email Not Received

1. Check spam folder
2. Verify sender email in SendGrid dashboard
3. Check SendGrid delivery status
4. Review OpenAI traces for errors

### Import Errors

Make sure you're in the project directory and have activated your virtual environment:

```bash
cd ai-sales-automation-agent
pip install -r requirements.txt
```

## Common Questions

**Q: Can I use a different email provider?**
A: Yes! Replace the `send_email` and `send_html_email` functions with your provider's API.

**Q: How much does this cost?**
A: SendGrid has a free tier (100 emails/day). OpenAI costs vary based on usage, but gpt-4o-mini is very affordable.

**Q: Can I add more agents?**
A: Absolutely! Just create new Agent instances with different instructions and add them to your workflow.

**Q: Is this production-ready?**
A: This is an educational demonstration. For production use, add error handling, rate limiting, logging, and monitoring.

## Resources

- [Full Documentation](README.md)
- [OpenAI Agents SDK Docs](https://platform.openai.com/docs/agents)
- [SendGrid API Docs](https://docs.sendgrid.com/)
- [View Traces](https://platform.openai.com/traces)

## Support

- GitHub Issues: https://github.com/csg09/ai-sales-automation-agent/issues
- OpenAI Platform: https://platform.openai.com/docs

---

**Ready to build?** Start with `basic_sales_agent.py` and work your way up to `automated_sdr.py`!
