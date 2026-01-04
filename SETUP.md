# Detailed Setup Guide

This guide provides comprehensive setup instructions for the AI Sales Automation Agent project.

## Table of Contents

- [System Requirements](#system-requirements)
- [Python Environment Setup](#python-environment-setup)
- [API Keys Configuration](#api-keys-configuration)
- [SendGrid Setup](#sendgrid-setup)
- [OpenAI Setup](#openai-setup)
- [Verification](#verification)
- [Troubleshooting](#troubleshooting)

## System Requirements

### Minimum Requirements

- **Operating System**: Windows 10+, macOS 10.14+, or Linux
- **Python**: Version 3.8 or higher
- **Memory**: 4GB RAM (8GB recommended)
- **Internet**: Stable connection for API calls

### Check Your Python Version

```bash
python --version
# or
python3 --version
```

If Python is not installed, download it from [python.org](https://www.python.org/downloads/)

## Python Environment Setup

### Option 1: Using Virtual Environment (Recommended)

Create an isolated Python environment:

```bash
# Create virtual environment
python -m venv venv

# Activate on macOS/Linux
source venv/bin/activate

# Activate on Windows
venv\Scripts\activate

# Your prompt should now show (venv)
```

### Option 2: Using Conda

If you use Anaconda or Miniconda:

```bash
# Create conda environment
conda create -n sales-agent python=3.11

# Activate environment
conda activate sales-agent
```

### Install Dependencies

```bash
# Ensure you're in the project directory
cd ai-sales-automation-agent

# Install required packages
pip install -r requirements.txt

# Verify installation
pip list
```

You should see:
- openai
- python-dotenv
- sendgrid
- asyncio

## API Keys Configuration

### 1. Create Environment File

```bash
# Copy the template
cp .env.example .env
```

### 2. Edit the Environment File

Open `.env` in your text editor and add your keys:

```env
# OpenAI Configuration
OPENAI_API_KEY=sk-proj-xxxxxxxxxxxxxxxxxxxxx

# SendGrid Configuration
SENDGRID_API_KEY=SG.xxxxxxxxxxxxxxxxxxxxx

# Email Addresses
SENDER_EMAIL=your-verified@email.com
RECIPIENT_EMAIL=recipient@email.com
```

**Security Note**: Never commit `.env` to version control!

## SendGrid Setup

### Step 1: Create Account

1. Visit [SendGrid](https://sendgrid.com/)
2. Click "Start for Free"
3. Complete registration (email verification required)

### Step 2: Verify Sender Email

This is **critical** - SendGrid won't send emails without verification:

1. Log into SendGrid dashboard
2. Navigate to: **Settings** → **Sender Authentication**
3. Click **"Verify a Single Sender"**
4. Fill in your details:
   - From Name: Your Name
   - From Email: your@email.com
   - Reply To: same or different email
   - Company Address: Your address
5. Check your email for verification link
6. Click verification link

**Wait for "Verified" status before proceeding!**

### Step 3: Create API Key

1. Navigate to: **Settings** → **API Keys**
2. Click **"Create API Key"**
3. Settings:
   - Name: "Sales Agent Key" (or your choice)
   - Permissions: "Full Access" (or "Mail Send" for production)
4. Click **"Create & View"**
5. **Copy the key immediately** (you won't see it again!)
6. Add to your `.env` file

### Step 4: Configure Email Addresses

In your `.env` file:

```env
# Use your VERIFIED sender email
SENDER_EMAIL=your-verified@email.com

# Can be any email you want to send to
RECIPIENT_EMAIL=test@email.com
```

## OpenAI Setup

### Step 1: Create Account

1. Visit [OpenAI Platform](https://platform.openai.com/)
2. Sign up or log in
3. Add payment method (required for API access)

### Step 2: Create API Key

1. Navigate to [API Keys](https://platform.openai.com/api-keys)
2. Click **"Create new secret key"**
3. Settings:
   - Name: "Sales Automation Agent"
   - Permissions: "All" (or customize)
4. Click **"Create secret key"**
5. **Copy the key immediately**
6. Add to your `.env` file

### Step 3: Set Usage Limits (Recommended)

1. Go to [Usage Limits](https://platform.openai.com/account/limits)
2. Set monthly budget limit
3. Enable email notifications

**Note**: gpt-4o-mini is very cost-effective (~$0.15 per 1M input tokens)

## Verification

### Step 1: Verify Environment Variables

```bash
# On macOS/Linux
cat .env

# On Windows
type .env
```

Ensure all four variables are set with real values.

### Step 2: Test Email Configuration

```bash
python test_email.py
```

**Expected Output:**
```
============================================================
SendGrid Email Configuration Test
============================================================

✅ Success! Test email sent successfully.
   Status Code: 202
   From: your@email.com
   To: recipient@email.com

ℹ️  Check your email inbox (and spam folder) for the test message.

============================================================
```

**If you see errors**, see [Troubleshooting](#troubleshooting) below.

### Step 3: Check Email Inbox

1. Check recipient email inbox
2. **Check spam/junk folder** (emails often go there initially)
3. If found in spam, mark as "Not Spam"

### Step 4: Test Basic Agent

```bash
python basic_sales_agent.py
```

This should run three demonstrations without errors.

### Step 5: View OpenAI Traces

1. Visit [OpenAI Traces](https://platform.openai.com/traces)
2. You should see your test runs
3. Click on a trace to see details

## Troubleshooting

### Common Issues

#### SSL Certificate Errors

**Error**: `SSL: CERTIFICATE_VERIFY_FAILED`

**Solution 1** (Windows/Mac):
```bash
pip install --upgrade certifi
```

Then add to your Python script:
```python
import certifi
import os
os.environ['SSL_CERT_FILE'] = certifi.where()
```

**Solution 2** (Mac specific):
```bash
/Applications/Python\ 3.x/Install\ Certificates.command
```

#### Environment Variables Not Loading

**Error**: `SENDGRID_API_KEY not found`

**Solutions**:
1. Ensure `.env` file is in the project root directory
2. Check file name is exactly `.env` (not `.env.txt`)
3. Verify no extra spaces around `=` in `.env`
4. Try loading explicitly:
   ```python
   load_dotenv(override=True)
   ```

#### SendGrid 401 Unauthorized

**Error**: Status code 401 from SendGrid

**Solutions**:
1. Verify API key is correct (no extra spaces)
2. Check API key permissions include "Mail Send"
3. Create a new API key if needed

#### SendGrid 403 Forbidden

**Error**: Status code 403 from SendGrid

**Solutions**:
1. Verify sender email is verified
2. Check SendGrid dashboard for account status
3. Ensure you're not on free trial with expired verification

#### No Email Received

**Possible Causes**:
1. Email in spam folder (check there first!)
2. Sender email not verified
3. Incorrect recipient email
4. SendGrid account issues

**Debug Steps**:
1. Check SendGrid dashboard → Activity
2. Look for email in Activity Feed
3. Check for delivery errors
4. Review OpenAI traces for API errors

#### Import Errors

**Error**: `ModuleNotFoundError: No module named 'agents'`

**Solutions**:
1. Ensure you installed requirements:
   ```bash
   pip install -r requirements.txt
   ```
2. Verify you're using the correct Python environment
3. Check that virtual environment is activated

#### OpenAI API Errors

**Error**: `AuthenticationError` or `RateLimitError`

**Solutions**:
1. Verify API key is correct
2. Check billing is set up on OpenAI account
3. Verify you have available credits
4. Check rate limits on your account

### Getting Help

If you're still experiencing issues:

1. **Check Documentation**: Review README.md and QUICKSTART.md
2. **Search Issues**: Look for similar issues on GitHub
3. **Create Issue**: Open a new issue with:
   - Error message (remove sensitive info)
   - Steps to reproduce
   - Your environment details
   - What you've already tried

### Verification Checklist

Before running the main scripts, verify:

- [ ] Python 3.8+ installed
- [ ] Virtual environment activated
- [ ] Dependencies installed (`pip list` shows all packages)
- [ ] `.env` file exists with all four variables
- [ ] SendGrid sender email verified (check dashboard)
- [ ] OpenAI API key valid (check dashboard)
- [ ] Test email sent successfully (status 202)
- [ ] Test email received (check inbox and spam)
- [ ] OpenAI traces visible in platform

## Next Steps

Once setup is complete:

1. **Review**: Read through `basic_sales_agent.py` to understand the code
2. **Customize**: Modify agent instructions to fit your use case
3. **Experiment**: Try different prompts and configurations
4. **Extend**: Add new agents, tools, or features
5. **Share**: Contribute improvements back to the project

## Additional Resources

- [SendGrid Documentation](https://docs.sendgrid.com/)
- [OpenAI API Documentation](https://platform.openai.com/docs)
- [OpenAI Agents SDK](https://platform.openai.com/docs/agents)
- [Python Virtual Environments](https://docs.python.org/3/tutorial/venv.html)

---

**Need help?** Open an issue on GitHub or check the troubleshooting section above.
