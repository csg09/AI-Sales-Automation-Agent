# Contributing to AI Sales Automation Agent

Thank you for your interest in contributing! This document provides guidelines and instructions for contributing to this project.

## How to Contribute

### Reporting Bugs

If you find a bug, please create an issue with:

- Clear description of the problem
- Steps to reproduce
- Expected vs actual behavior
- Your environment (OS, Python version, etc.)
- Relevant error messages or screenshots

### Suggesting Enhancements

Feature requests are welcome! Please include:

- Clear description of the feature
- Use case and benefits
- Potential implementation approach
- Any relevant examples or references

### Submitting Pull Requests

1. **Fork the repository**
   ```bash
   git clone https://github.com/csg09/ai-sales-automation-agent.git
   cd ai-sales-automation-agent
   ```

2. **Create a feature branch**
   ```bash
   git checkout -b feature/your-feature-name
   ```

3. **Make your changes**
   - Follow the code style guidelines below
   - Add tests if applicable
   - Update documentation as needed

4. **Test your changes**
   ```bash
   python test_email.py
   python basic_sales_agent.py
   python automated_sdr.py
   ```

5. **Commit your changes**
   ```bash
   git add .
   git commit -m "Add feature: description of your changes"
   ```

6. **Push to your fork**
   ```bash
   git push origin feature/your-feature-name
   ```

7. **Create a Pull Request**
   - Go to the original repository
   - Click "New Pull Request"
   - Select your feature branch
   - Provide a clear description of changes

## Code Style Guidelines

### Python Code Style

- Follow PEP 8 guidelines
- Use meaningful variable and function names
- Add docstrings to all functions and classes
- Keep functions focused and single-purpose
- Use type hints where appropriate

**Example:**

```python
@function_tool
def send_notification(message: str, priority: str = "normal") -> Dict[str, str]:
    """
    Send a notification with the given message and priority.
    
    Args:
        message: The notification message to send
        priority: Priority level (normal, high, urgent)
        
    Returns:
        Dictionary with status and priority confirmation
    """
    # Implementation here
    return {"status": "sent", "priority": priority}
```

### Documentation Style

- Use clear, concise language
- Include code examples where helpful
- Keep README and docs up to date
- Add comments for complex logic

### Commit Messages

Follow conventional commit format:

- `feat:` New feature
- `fix:` Bug fix
- `docs:` Documentation changes
- `style:` Code style changes (formatting, etc.)
- `refactor:` Code refactoring
- `test:` Adding or updating tests
- `chore:` Maintenance tasks

**Examples:**
```
feat: Add support for multiple email providers
fix: Resolve SSL certificate error on Windows
docs: Update quickstart guide with troubleshooting
refactor: Simplify agent tool creation logic
```

## Enhancement Ideas

Here are some areas where contributions would be especially valuable:

### High Priority
- [ ] Support for additional email providers (Resend, Mailgun, etc.)
- [ ] Webhook handler for email replies
- [ ] Bulk email sending with mail merge
- [ ] Rate limiting and retry logic
- [ ] Comprehensive error handling

### Medium Priority
- [ ] A/B testing framework for emails
- [ ] Email template library
- [ ] CRM integration examples
- [ ] Response tracking and analytics
- [ ] Multi-language support

### Nice to Have
- [ ] Web UI for email preview
- [ ] Email performance dashboard
- [ ] Advanced personalization options
- [ ] Integration with popular sales tools
- [ ] Automated testing suite

## Development Setup

### Virtual Environment

It's recommended to use a virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### Environment Variables

Create a `.env` file for testing:

```env
OPENAI_API_KEY=your_test_key
SENDGRID_API_KEY=your_test_key
SENDER_EMAIL=test@example.com
RECIPIENT_EMAIL=test@example.com
```

**Never commit your `.env` file or real API keys!**

### Running Tests

Before submitting a PR, ensure all examples run successfully:

```bash
python test_email.py
python basic_sales_agent.py
python automated_sdr.py
python examples/parallel_execution.py
python examples/tool_usage.py
```

## Code of Conduct

### Our Standards

- Be respectful and inclusive
- Welcome newcomers
- Accept constructive criticism
- Focus on what's best for the community
- Show empathy towards others

### Unacceptable Behavior

- Harassment or discriminatory language
- Trolling or insulting comments
- Personal or political attacks
- Publishing others' private information
- Other conduct inappropriate in a professional setting

## Questions?

If you have questions about contributing:

- Open a GitHub issue with the `question` label
- Check existing issues and discussions
- Review the main README.md documentation

## Recognition

Contributors will be recognized in the project documentation. Thank you for helping improve this project!

## License

By contributing, you agree that your contributions will be licensed under the MIT License.
