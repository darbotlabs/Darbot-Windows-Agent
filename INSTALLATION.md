# 📋 Installation Guide - Darbot Windows Agent

<div align="center">
  <h2>📋 Complete Installation Guide</h2>
</div>

This guide provides comprehensive installation instructions for all supported methods to get Darbot Windows Agent running on your system.

## 📋 Table of Contents

- [Prerequisites](#prerequisites)
- [Method 1: pip Installation (Recommended)](#method-1-pip-installation-recommended)
- [Method 2: UV Installation](#method-2-uv-installation)
- [Method 3: Development Installation](#method-3-development-installation)
- [Configuration](#configuration)
- [Testing Your Installation](#testing-your-installation)
- [Common Issues](#common-issues)

## Prerequisites

Before installing Darbot Windows Agent, ensure you have the following:

### System Requirements
- **Windows 10** or **Windows 11** (Windows 11 recommended)
- **English Windows locale** for consistent UI Automation tree
- **Administrator privileges** (for some installation steps)

### Software Dependencies
- **Python 3.12+** (required)
- **Git** (for development installation)

### Check Your System

```bash
# Check Python version
python --version

# Check if Git is installed (for development)
git --version
```

## Method 1: pip Installation (Recommended)

The pip installation is the easiest method for most users.

### Step 1: Install the Package

```bash
pip install darbot-windows-agent
```

### Step 2: Test the Installation

```bash
python -c "import darbot_windows_agent; print('Installation successful!')"
```

## Method 2: UV Installation

UV is a modern, fast Python package manager that provides faster dependency management.

### Step 1: Install UV

```bash
# Install UV using pip
pip install uv
```

### Step 2: Install the Package

```bash
uv pip install darbot-windows-agent
```

### Step 3: Test the Installation

```bash
python -c "import darbot_windows_agent; print('Installation successful!')"
```

## Method 3: Development Installation

Use this method if you want to contribute or modify the code.

### Step 1: Clone the Repository

```bash
git clone https://github.com/darbotlabs/darbot-windows-agent.git
cd darbot-windows-agent
```

### Step 2: Install in Development Mode

```bash
# Using pip
pip install -e .

# Or using UV
uv pip install -e .
```

### Step 3: Test the Installation

```bash
python -c "import darbot_windows_agent; print('Development installation successful!')"
```

## Configuration

### Environment Setup

1. **Create a `.env` file** in your project directory:

```bash
# .env
GOOGLE_API_KEY=your_google_api_key_here
```

2. **Set up your API keys** for the LLM services you plan to use:
   - Google Gemini: `GOOGLE_API_KEY`
   - OpenAI: `OPENAI_API_KEY`
   - Groq: `GROQ_API_KEY`
   - Ollama: Configure local installation

### Basic Usage Setup

Create a basic script to test the agent:

```python
# test_agent.py
from langchain_google_genai import ChatGoogleGenerativeAI
from darbot_windows_agent.agent import Agent
from dotenv import load_dotenv

load_dotenv()

def test_agent():
    llm = ChatGoogleGenerativeAI(model='gemini-2.0-flash')
    agent = Agent(llm=llm, browser='chrome', use_vision=False)
    
    # Test with a simple query
    result = agent.invoke(query="What applications are currently running?")
    print(result.content)

if __name__ == "__main__":
    test_agent()
```

## Testing Your Installation

### Basic Import Test

```bash
python -c "import darbot_windows_agent; print('✅ Import successful')"
```

### Component Test

```bash
python -c "
from darbot_windows_agent.agent import Agent
from darbot_windows_agent.desktop import Desktop
print('✅ All components imported successfully')
"
```

### Agent Test

Run the basic usage example from the main README:

```python
python main.py
# Enter a simple query like: "Tell me what's on my desktop"
```

## Common Issues

### "No module named 'darbot_windows_agent'"

**Solution:**
1. Ensure the package is installed: `pip list | grep darbot-windows-agent`
2. Check Python path: `python -c "import sys; print(sys.path)"`
3. Reinstall: `pip uninstall darbot-windows-agent && pip install darbot-windows-agent`

### Dependency Resolution Errors

**Error:**
```
ERROR: Could not find a version that satisfies the requirement...
```

**Solutions:**

1. **Upgrade pip:**
   ```bash
   python -m pip install --upgrade pip
   ```

2. **Use UV for better dependency resolution:**
   ```bash
   pip install uv
   uv pip install darbot-windows-agent
   ```

3. **Install with no dependencies and add them manually:**
   ```bash
   pip install darbot-windows-agent --no-deps
   pip install langchain langchain-google-genai pyautogui uiautomation
   ```

### Permission Errors

**Solutions:**

1. **Run as Administrator** for initial installation
2. **Use user installation:**
   ```bash
   pip install --user darbot-windows-agent
   ```

### Import Errors During Runtime

**Common missing dependencies:**

```bash
# Install core dependencies manually
pip install langchain>=0.3.25
pip install langchain-google-genai>=2.1.5  
pip install pyautogui>=0.9.54
pip install uiautomation>=2.0.28
pip install pillow>=11.2.1
pip install python-dotenv
```

### UI Automation Issues

**Solutions:**

1. **Set Windows to English locale**
2. **Run with administrator privileges**
3. **Ensure Windows UI Automation is enabled**
4. **Check antivirus software** - may block automation tools

### Performance Issues

**Solutions:**

1. **Close unnecessary applications** to free up system resources
2. **Adjust timing settings** in agent configuration if needed
3. **Monitor system resources** during agent execution

## Getting Help

If you're still having issues:

1. Check the [main README](README.md) for basic usage examples
2. Review the [Issues on GitHub](https://github.com/darbotlabs/darbot-windows-agent/issues)
3. Create a new issue with:
   - Your Python version (`python --version`)
   - Your operating system version
   - Complete error messages
   - Steps to reproduce the issue

## Next Steps

After successful installation:

- Review the [Basic Usage](README.md#basic-usage) section in the main README
- Try the example scripts and demos
- Check the [Contributing Guide](CONTRIBUTING.md) if you want to contribute
- Explore the agent capabilities with your preferred LLM