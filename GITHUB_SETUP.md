# GitHub Setup Guide

Step-by-step instructions to publish this project to your GitHub account.

## Prerequisites

- Git installed on your computer
- GitHub account (sign up at [github.com](https://github.com))
- Project files downloaded to your computer

## Step 1: Prepare Your Local Repository

### 1.1 Open Terminal/Command Prompt

Navigate to your project directory:

```bash
cd path/to/ai-sales-automation-agent
```

### 1.2 Initialize Git Repository

```bash
git init
```

### 1.3 Add All Files

```bash
git add .
```

### 1.4 Create Initial Commit

```bash
git commit -m "Initial commit: AI Sales Automation Agent"
```

## Step 2: Create GitHub Repository

### 2.1 Create New Repository

1. Go to [github.com](https://github.com)
2. Click the **+** icon (top right)
3. Select **"New repository"**

### 2.2 Configure Repository

Fill in the details:

- **Repository name**: `ai-sales-automation-agent`
- **Description**: `Intelligent multi-agent system for automated sales email generation using OpenAI Agents SDK`
- **Visibility**: Choose Public or Private
- **DO NOT** initialize with README, .gitignore, or license (we already have these)

Click **"Create repository"**

## Step 3: Connect Local to GitHub

### 3.1 Add Remote

Copy the repository URL from GitHub (should look like):
```
https://github.com/csg09/ai-sales-automation-agent.git
```

Then run:

```bash
git remote add origin https://github.com/csg09/ai-sales-automation-agent.git
```

### 3.2 Verify Remote

```bash
git remote -v
```

You should see:
```
origin  https://github.com/csg09/ai-sales-automation-agent.git (fetch)
origin  https://github.com/csg09/ai-sales-automation-agent.git (push)
```

## Step 4: Push to GitHub

### 4.1 Push Main Branch

```bash
git branch -M main
git push -u origin main
```

### 4.2 Verify Upload

Go to your GitHub repository page. You should see all your files!

## Step 5: Configure Repository Settings

### 5.1 Add Topics

On your repository page:
1. Click the gear icon next to "About"
2. Add topics: `ai`, `openai`, `agents`, `automation`, `sales`, `python`, `sendgrid`, `machine-learning`
3. Click "Save changes"

### 5.2 Update Description

Set repository description:
```
Intelligent multi-agent system for automated sales email generation using OpenAI Agents SDK
```

Add website (optional):
```
https://github.com/csg09/ai-sales-automation-agent
```

### 5.3 Enable Discussions (Optional)

Settings → General → Features → Check "Discussions"

## Step 6: Add Repository Badges (Optional)

Edit your README.md to add badges at the top:

```markdown
# AI Sales Automation Agent

[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenAI](https://img.shields.io/badge/OpenAI-Agents_SDK-412991.svg)](https://platform.openai.com/docs/agents)

[Rest of README...]
```

Commit and push the changes:

```bash
git add README.md
git commit -m "Add repository badges"
git push
```

## Step 7: Protect Your Secrets

### 7.1 Verify .gitignore

Ensure `.env` is listed in `.gitignore` (already done in this project)

### 7.2 Check for Exposed Secrets

```bash
# Search for potential API keys in git history
git log --all --full-history --source --pretty=format:"%H" -- .env
```

If this returns anything, your `.env` was committed. See "Emergency: Remove Secrets" below.

### 7.3 Never Commit These Files

- `.env` (API keys and secrets)
- `venv/` or `env/` (virtual environment)
- `__pycache__/` (Python cache)
- `.DS_Store` (Mac system files)

All of these are already in `.gitignore`

## Emergency: Remove Secrets from History

If you accidentally committed your `.env` file:

### Option 1: If Just Pushed

```bash
# Remove the last commit
git reset --hard HEAD~1

# Force push
git push --force
```

### Option 2: Remove File from History

```bash
# Install git-filter-repo
pip install git-filter-repo

# Remove .env from all history
git filter-repo --path .env --invert-paths

# Force push
git push --force
```

**IMPORTANT**: After removing secrets, regenerate all API keys!

## Working with the Repository

### Making Changes

```bash
# 1. Make your code changes

# 2. Check what changed
git status

# 3. Add changes
git add .

# 4. Commit with descriptive message
git commit -m "feat: Add support for multiple email providers"

# 5. Push to GitHub
git push
```

### Creating Branches

For new features:

```bash
# Create and switch to new branch
git checkout -b feature/email-templates

# Make changes, commit

# Push branch to GitHub
git push -u origin feature/email-templates

# Create Pull Request on GitHub
```

### Syncing with GitHub

```bash
# Pull latest changes
git pull origin main
```

## Customizing Your Repository

### Update Personal Information

Search and replace in all files:

1. **GitHub Username**
   - Replace `csg09` with your username
   - Files to check: README.md, CONTRIBUTING.md, etc.

2. **Contact Information**
   - Update email addresses in test_email.py
   - Update contact section in README.md

3. **Repository Links**
   - Update all GitHub links with your username

### Customize Content

1. **Agent Instructions**: Modify in Python files to match your use case
2. **Company Information**: Change "ComplAI" to your company/project
3. **Documentation**: Update examples to match your implementation

## Repository Maintenance

### Regular Updates

```bash
# Update dependencies
pip install --upgrade -r requirements.txt
pip freeze > requirements.txt

# Commit updated requirements
git add requirements.txt
git commit -m "chore: Update dependencies"
git push
```

### Tagging Releases

When you reach a milestone:

```bash
# Create annotated tag
git tag -a v1.0.0 -m "Version 1.0.0 - Initial release"

# Push tag to GitHub
git push origin v1.0.0
```

Then create a release on GitHub:
1. Go to repository → Releases
2. Click "Draft a new release"
3. Select your tag
4. Add release notes
5. Publish release

## GitHub Features to Enable

### 1. Branch Protection

Settings → Branches → Add rule:
- Require pull request reviews
- Require status checks
- Prevent force pushes

### 2. Security Alerts

Settings → Security & analysis:
- Enable Dependabot alerts
- Enable Dependabot security updates

### 3. Issue Templates

Create `.github/ISSUE_TEMPLATE/bug_report.md`

### 4. Pull Request Template

Create `.github/pull_request_template.md`

## Showcase Your Project

### 1. Pin to Profile

On your GitHub profile:
- Click "Customize your pins"
- Select this repository

### 2. Add to Portfolio

Include in your:
- GitHub README.md profile
- LinkedIn projects
- Personal website
- Resume/CV

### 3. Share on Social Media

Tweet/post about it with:
- Project link
- Key features
- What you learned
- Screenshots/demos

## Common Git Commands

```bash
# Check status
git status

# View commit history
git log

# View differences
git diff

# Discard local changes
git checkout -- filename

# Update from remote
git pull

# View branches
git branch -a

# Switch branches
git checkout branch-name

# Merge branches
git merge branch-name
```

## Troubleshooting

### Authentication Issues

If prompted for username/password repeatedly:

**Use Personal Access Token**:
1. GitHub → Settings → Developer settings → Personal access tokens
2. Generate new token with 'repo' scope
3. Use token as password when prompted

Or configure Git credential helper:
```bash
git config --global credential.helper cache
```

### Large File Issues

If you get "file too large" errors:

1. Add to `.gitignore`
2. Remove from staging:
   ```bash
   git rm --cached large-file
   ```

### Merge Conflicts

If you get merge conflicts:

1. Open conflicted files
2. Look for `<<<<<<<`, `=======`, `>>>>>>>`
3. Resolve conflicts
4. Stage resolved files: `git add .`
5. Complete merge: `git commit`

## Resources

- [Git Documentation](https://git-scm.com/doc)
- [GitHub Guides](https://guides.github.com/)
- [GitHub Skills](https://skills.github.com/)
- [Pro Git Book](https://git-scm.com/book/en/v2)

## Next Steps

1. ✅ Repository created and pushed to GitHub
2. 📝 Customize README with your information
3. 🏷️ Add topics and badges
4. 🔒 Verify no secrets in history
5. 📢 Share your project!

---

**Congratulations!** Your project is now on GitHub and ready to showcase your AI development skills!
