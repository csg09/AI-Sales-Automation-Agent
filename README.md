# AI Sales Automation Agent

An intelligent multi-agent system for generating, optimizing, and sending cold sales emails using OpenAI's Agents SDK. This project demonstrates agentic AI patterns including parallel agent execution, tool use, and agent handoffs.

## 🎯 Overview

This project implements an automated Sales Development Representative (SDR) system that:
- Generates multiple cold email variations using different writing styles
- Automatically selects the best email through AI evaluation
- Formats emails with AI-generated subjects and HTML layouts
- Sends emails through SendGrid API
- Provides full observability through OpenAI traces

## ✨ Features

- **Multi-Agent Architecture**: Three specialized sales agents with distinct writing styles (professional, engaging, concise)
- **Parallel Execution**: Concurrent email generation for faster results
- **AI-Powered Selection**: Automated evaluation to choose the most effective email
- **Tool Integration**: Function calling for email sending capabilities
- **Agent Handoffs**: Seamless delegation between email generation and formatting agents
- **HTML Conversion**: Automatic conversion from plain text to professional HTML emails
- **Subject Line Generation**: AI-optimized email subjects
- **Observability**: Full tracing through OpenAI platform

## 🏗️ Architecture

### Agentic Design Patterns

This project implements several key agentic AI patterns:

1. **Planning Pattern**: Sales Manager agent coordinates the workflow
2. **Parallel Execution**: Multiple agents run concurrently for efficiency
3. **Tool Use**: Function calling for external integrations (SendGrid)
4. **Agent Collaboration**: Agents work together via tools and handoffs
5. **Handoffs**: Control delegation from Sales Manager to Email Manager

### Agent Structure

```
Sales Manager (Orchestrator)
├── Professional Sales Agent → Tool
├── Engaging Sales Agent → Tool
├── Busy Sales Agent → Tool
└── Email Manager (Handoff)
    ├── Subject Writer → Tool
    ├── HTML Converter → Tool
    └── send_html_email() → Function Tool
```

## 🚀 Getting Started

### Prerequisites

- Python 3.8+
- OpenAI API key
- SendGrid account and API key

### Installation

1. Clone the repository:
```bash
git clone https://github.com/csg09/ai-sales-automation-agent.git
cd ai-sales-automation-agent
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Set up environment variables:
```bash
cp .env.example .env
# Edit .env and add your API keys
```

4. Configure SendGrid:
   - Create a free account at [SendGrid](https://sendgrid.com/)
   - Navigate to: Settings → API Keys → Create API Key
   - Add your API key to `.env`
   - Verify your sender email: Settings → Sender Authentication → Verify a Single Sender

### Quick Start

Run the test email script to verify your setup:

```bash
python test_email.py
```

Run the basic sales agent workflow:

```bash
python basic_sales_agent.py
```

Run the full automated SDR system:

```bash
python automated_sdr.py
```

## 📁 Project Structure

```
ai-sales-automation-agent/
├── README.md                  # This file
├── LICENSE                    # MIT License
├── requirements.txt           # Python dependencies
├── .env.example              # Environment variables template
├── .gitignore                # Git ignore rules
├── basic_sales_agent.py      # Simple agent workflow
├── automated_sdr.py          # Full SDR system with handoffs
├── test_email.py             # Email configuration test
└── examples/
    ├── parallel_execution.py  # Parallel agent demo
    └── tool_usage.py         # Tool integration examples
```

## 🔧 Configuration

### Environment Variables

Create a `.env` file with the following variables:

```env
OPENAI_API_KEY=your_openai_api_key_here
SENDGRID_API_KEY=your_sendgrid_api_key_here
SENDER_EMAIL=your_verified_sender@example.com
RECIPIENT_EMAIL=your_recipient@example.com
```

### Customization

You can customize the agents by modifying their instructions in the respective Python files:

- **Professional Agent**: Formal, serious tone
- **Engaging Agent**: Witty, humorous approach
- **Busy Agent**: Concise, direct messaging

## 📊 Monitoring and Debugging

All agent executions are traced in the OpenAI platform. View your traces at:

https://platform.openai.com/traces

Traces provide:
- Agent decision-making process
- Tool calls and responses
- Handoff transitions
- Performance metrics

## 🛠️ Troubleshooting

### SSL Certificate Errors

If you encounter SSL certificate errors:

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

1. Check your spam folder
2. Verify sender authentication in SendGrid
3. Confirm API key is correct
4. Check SendGrid dashboard for delivery status
5. Review OpenAI traces for errors

### Alternative Email Provider

If SendGrid doesn't work for you, consider using [Resend](https://resend.com/) as an alternative. Check the `examples/` directory for implementation.

## 🎓 Learning Outcomes

This project demonstrates:

- **Agentic Workflows**: Multi-agent coordination and planning
- **Tool Integration**: Converting functions into agent-callable tools
- **Agent Handoffs**: Delegating control between specialized agents
- **Async Programming**: Parallel execution with asyncio
- **Production Patterns**: Error handling, environment management, and logging

## 🔄 Workflow

1. **Sales Manager** receives request to send cold email
2. **Three Sales Agents** generate email drafts in parallel
3. **Sales Manager** evaluates and selects best email
4. **Email Manager** receives handoff with winning email
5. **Subject Writer** generates optimized subject line
6. **HTML Converter** formats email body
7. **send_html_email** tool sends final formatted email

## 🤝 Contributing

Contributions are welcome! Here are some ideas for enhancements:

- [ ] Add more sales agent personalities
- [ ] Implement mail merge for bulk sending
- [ ] Add webhook handler for email replies
- [ ] Create A/B testing framework
- [ ] Integrate with CRM systems
- [ ] Add response tracking and analytics
- [ ] Implement rate limiting and retry logic

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Built using [OpenAI Agents SDK](https://platform.openai.com/docs/agents)
- Email delivery via [SendGrid](https://sendgrid.com/)
- Inspired by modern agentic AI patterns and workflows

## 📧 Contact

- GitHub: [@csg09](https://github.com/csg09)
- Project Link: [https://github.com/csg09/ai-sales-automation-agent](https://github.com/csg09/ai-sales-automation-agent)

## 🔗 Related Projects

Check out my other AI projects:
- [OpenAI Agents SDK Examples](https://github.com/csg09)
- [Multi-Model LLM Comparison](https://github.com/csg09)
- [Agentic AI Workflows](https://github.com/csg09)

---

**Note**: This is an educational project demonstrating agentic AI patterns. Always follow email marketing best practices and comply with anti-spam regulations (CAN-SPAM, GDPR, etc.) when using automated email systems.
