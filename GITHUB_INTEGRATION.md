# GitHub CLI and Model Selection Integration

This document describes the GitHub CLI and model selection features integrated into the Darbot Windows Agent.

## Features Added

### 1. GitHub CLI Tool Integration

The agent now includes a GitHub CLI tool that allows you to execute GitHub CLI commands directly from the agent.

**Capabilities:**
- Execute any `gh` command through the agent
- Automatic GitHub CLI installation detection
- Authentication status checking
- Repository management
- Pull request and issue operations

**Examples:**
```python
# Check GitHub authentication status
agent.invoke("gh auth status")

# List repositories
agent.invoke("gh repo list")

# List pull requests
agent.invoke("gh pr list")

# View repository details
agent.invoke("gh repo view")
```

### 2. Model Selection Interface

A VSCode GitHub Copilot-style model selection interface that supports multiple LLM providers.

**Supported Providers:**

#### GitHub Copilot Models (requires GitHub authentication)
- GPT-4 (GitHub Copilot)
- GPT-4 Turbo (GitHub Copilot) 
- GPT-3.5 Turbo (GitHub Copilot)

#### Direct Provider Models
- **OpenAI**: GPT-4, GPT-4 Turbo, GPT-3.5 Turbo
- **Google**: Gemini 2.0 Flash, Gemini 1.5 Pro
- **Groq**: Llama 3.1 70B, Mixtral 8x7B
- **Ollama**: Local models (Llama 3, Code Llama)

### 3. GitHub Authentication

Integrated GitHub authentication management compatible with GitHub CLI.

## Usage

### Enhanced Main Application

Use the new `main_enhanced.py` for the full experience:

```bash
python main_enhanced.py
```

This provides:
- Interactive model selection menu
- GitHub authentication setup
- Enhanced UI with provider grouping
- Special commands support

### Programmatic Usage

```python
from darbot_windows_agent.agent import Agent
from darbot_windows_agent.github.models import ModelSelector
from darbot_windows_agent.github.auth import GitHubAuth

# Initialize model selector
model_selector = ModelSelector()

# List available models
models = model_selector.list_available_models()
for model in models:
    print(f"{model['name']} - {'✅' if model['available'] else '❌'}")

# Select a model
model_selector.select_model('gpt-4')  # GitHub Copilot GPT-4

# Create LLM instance
llm = model_selector.create_llm()

# Initialize agent with model selector
agent = Agent(llm=llm, model_selector=model_selector)

# Use GitHub CLI commands
result = agent.invoke("gh auth status")
print(result.content)
```

### GitHub Authentication Setup

```python
from darbot_windows_agent.github.auth import GitHubAuth

github_auth = GitHubAuth()

# Check authentication status
if not github_auth.is_authenticated():
    # Login to GitHub
    result, success = github_auth.login()
    if success:
        print("GitHub authentication successful!")
```

## Special Commands in Enhanced Main

When using `main_enhanced.py`, you have access to special commands:

- `models` - Open model selection menu
- `github` - Quick GitHub authentication setup
- `quit` - Exit the application

## Environment Variables

The following environment variables are supported:

```bash
# For GitHub Copilot (uses GitHub CLI authentication)
# No additional API key needed

# For direct provider access
OPENAI_API_KEY=your_openai_key
GOOGLE_API_KEY=your_google_key  
GROQ_API_KEY=your_groq_key

# Ollama runs locally, no API key needed
```

## File Structure

```
darbot_windows_agent/
├── github/
│   ├── __init__.py          # Module exports
│   ├── auth.py              # GitHub authentication
│   ├── cli.py               # CLI tool exports
│   ├── models.py            # Model selector
│   └── views.py             # Pydantic schemas
├── agent/
│   ├── service.py           # Updated with model selector
│   └── tools/
│       ├── service.py       # Updated with GitHub CLI tool
│       └── views.py         # Updated with GitHub schemas
main_enhanced.py             # Enhanced main with model selection
```

## Dependencies

The integration uses existing dependencies and doesn't require additional packages beyond what's already in `pyproject.toml`. The key dependencies are:

- `langchain-openai` - For OpenAI and GitHub Copilot models
- `langchain-google-genai` - For Google models
- `langchain-groq` - For Groq models
- `langchain-ollama` - For local Ollama models
- `pydantic` - For data validation
- `subprocess` - For GitHub CLI execution

## GitHub CLI Installation

Users need to install GitHub CLI separately:

**Windows:**
```bash
winget install GitHub.cli
```

**Or download from:** https://cli.github.com/

## Security Considerations

- GitHub tokens are managed through GitHub CLI's secure token storage
- API keys are read from environment variables only
- No credentials are stored in code or logs
- GitHub CLI handles OAuth flow securely

## Backwards Compatibility

The integration is fully backwards compatible:
- Existing code using `Agent(llm=your_llm)` continues to work
- Model selector is optional and defaults to a new instance if not provided
- GitHub CLI tool is added to existing tools without affecting others