# 🚧 Troubleshooting Guide - Darbot Windows Agent

<div align="center">
  <h2>🚧 Comprehensive Troubleshooting Guide</h2>
</div>

This guide covers common issues and their solutions when using Darbot Windows Agent.

## 📋 Table of Contents

- [Installation Issues](#installation-issues)
- [Runtime Issues](#runtime-issues)
- [Agent Performance Issues](#agent-performance-issues)
- [UI Automation Issues](#ui-automation-issues)
- [LLM Integration Issues](#llm-integration-issues)
- [System Compatibility Issues](#system-compatibility-issues)
- [Debugging Tips](#debugging-tips)

## Installation Issues

### Package Not Found Error

**Error:**
```
ERROR: Could not find a version that satisfies the requirement darbot-windows-agent
```

**Solutions:**

1. **Check package name spelling:**
   ```bash
   pip install darbot-windows-agent  # Correct spelling
   ```

2. **Update pip:**
   ```bash
   python -m pip install --upgrade pip
   ```

3. **Use alternative installation methods:**
   ```bash
   # Try with UV
   pip install uv
   uv pip install darbot-windows-agent
   ```

### Dependency Resolution Conflicts

**Error:**
```
ERROR: pip's dependency resolver does not currently have a working solution...
```

**Solutions:**

1. **Install in clean environment:**
   ```bash
   python -m venv venv
   venv\Scripts\activate
   pip install darbot-windows-agent
   ```

2. **Use UV for better dependency resolution:**
   ```bash
   pip install uv
   uv pip install darbot-windows-agent
   ```

3. **Install core dependencies first:**
   ```bash
   pip install langchain>=0.3.25
   pip install langchain-google-genai>=2.1.5
   pip install darbot-windows-agent --no-deps
   ```

### Python Version Compatibility

**Error:**
```
ERROR: Package requires a different python version
```

**Solutions:**

1. **Check Python version:**
   ```bash
   python --version  # Should be 3.12+
   ```

2. **Upgrade Python:**
   - Download from [python.org](https://python.org)
   - Install Python 3.12 or higher

3. **Use pyenv (if available):**
   ```bash
   pyenv install 3.12.0
   pyenv local 3.12.0
   ```

## Runtime Issues

### Import Errors

**Error:**
```
ModuleNotFoundError: No module named 'darbot_windows_agent'
```

**Solutions:**

1. **Verify installation:**
   ```bash
   pip list | grep darbot-windows-agent
   ```

2. **Check Python path:**
   ```bash
   python -c "import sys; print('\n'.join(sys.path))"
   ```

3. **Reinstall package:**
   ```bash
   pip uninstall darbot-windows-agent
   pip install darbot-windows-agent
   ```

### Missing Dependencies

**Error:**
```
ModuleNotFoundError: No module named 'langchain'
```

**Solutions:**

1. **Install missing dependencies:**
   ```bash
   pip install langchain langchain-google-genai
   pip install pyautogui uiautomation
   pip install pillow python-dotenv
   ```

2. **Reinstall with all dependencies:**
   ```bash
   pip install darbot-windows-agent --force-reinstall
   ```

### Environment Variable Issues

**Error:**
```
API key not found or invalid
```

**Solutions:**

1. **Create `.env` file:**
   ```bash
   # .env
   GOOGLE_API_KEY=your_actual_api_key_here
   ```

2. **Check environment variables:**
   ```python
   import os
   print(f"GOOGLE_API_KEY: {os.getenv('GOOGLE_API_KEY')}")
   ```

3. **Load environment variables:**
   ```python
   from dotenv import load_dotenv
   load_dotenv()  # Call this before using the agent
   ```

## Agent Performance Issues

### Slow Response Times

**Symptoms:**
- Agent takes more than 10 seconds to respond
- Actions timeout frequently

**Solutions:**

1. **Check system resources:**
   ```bash
   # Windows Task Manager: Ctrl+Shift+Esc
   # Monitor CPU and Memory usage
   ```

2. **Close unnecessary applications:**
   - Close unused browser tabs
   - Stop background processes

3. **Adjust agent settings:**
   ```python
   agent = Agent(llm=llm, browser='chrome', use_vision=False)
   # Set use_vision=False for faster performance
   ```

4. **Use faster LLM models:**
   ```python
   # Use lighter models for better performance
   llm = ChatGoogleGenerativeAI(model='gemini-1.5-flash')
   ```

### High Memory Usage

**Solutions:**

1. **Monitor memory usage:**
   ```python
   import psutil
   print(f"Memory usage: {psutil.virtual_memory().percent}%")
   ```

2. **Restart agent periodically:**
   ```python
   # In long-running scripts, recreate agent instance
   del agent
   agent = Agent(llm=llm, browser='chrome')
   ```

3. **Optimize vision usage:**
   ```python
   # Only use vision when necessary
   agent = Agent(llm=llm, use_vision=False)
   ```

## UI Automation Issues

### Element Not Found Errors

**Error:**
```
Element not found on screen
```

**Solutions:**

1. **Check Windows locale:**
   - Set Windows display language to English
   - Restart the application after changing locale

2. **Adjust timing:**
   ```python
   import time
   time.sleep(2)  # Wait for UI to load
   agent.invoke(query="Your query here")
   ```

3. **Use specific element selectors:**
   - Be more specific in your queries
   - Use exact application names

### Permission Denied Errors

**Error:**
```
Access denied when trying to control application
```

**Solutions:**

1. **Run as Administrator:**
   - Right-click Python script
   - Select "Run as administrator"

2. **Check UAC settings:**
   - Temporarily lower UAC level for testing
   - Add Python to UAC exceptions

3. **Verify application accessibility:**
   - Some applications block automation
   - Try with different applications first

### Screen Resolution Issues

**Solutions:**

1. **Use standard resolution:**
   - Set screen resolution to 1920x1080 or similar
   - Avoid unusual screen scaling

2. **Check DPI settings:**
   - Set DPI scaling to 100%
   - Restart applications after changing DPI

## LLM Integration Issues

### API Authentication Errors

**Error:**
```
Authentication failed with LLM provider
```

**Solutions:**

1. **Verify API key:**
   ```python
   import os
   api_key = os.getenv('GOOGLE_API_KEY')
   print(f"API Key: {api_key[:10]}..." if api_key else "No API key found")
   ```

2. **Check API key format:**
   - Google: Should start with specific prefix
   - OpenAI: Should start with "sk-"
   - Ensure no extra spaces or characters

3. **Test API connection:**
   ```python
   from langchain_google_genai import ChatGoogleGenerativeAI
   llm = ChatGoogleGenerativeAI(model='gemini-2.0-flash')
   response = llm.invoke("Hello")
   print(response)
   ```

### Rate Limiting Issues

**Error:**
```
Rate limit exceeded
```

**Solutions:**

1. **Add delays between requests:**
   ```python
   import time
   time.sleep(1)  # Wait between agent calls
   ```

2. **Use different API keys:**
   - Rotate between multiple API keys
   - Upgrade to higher tier plans

### Model Not Available Errors

**Solutions:**

1. **Use available models:**
   ```python
   # Try different models
   llm = ChatGoogleGenerativeAI(model='gemini-1.5-pro')
   # or
   llm = ChatGoogleGenerativeAI(model='gemini-1.5-flash')
   ```

2. **Check model availability:**
   - Verify model is available in your region
   - Check provider documentation

## System Compatibility Issues

### Windows Version Compatibility

**Issues:**
- Features not working on older Windows versions
- UI Automation inconsistencies

**Solutions:**

1. **Upgrade to Windows 11:**
   - Best compatibility with modern automation

2. **Install Windows updates:**
   ```bash
   # Check for Windows updates
   winget list --upgrade-available
   ```

3. **Enable Windows features:**
   - Enable "Windows Subsystem for Linux" if needed
   - Update .NET Framework

### Antivirus Interference

**Symptoms:**
- Scripts suddenly stop working
- Permission denied errors
- Slow performance

**Solutions:**

1. **Add Python to antivirus exceptions:**
   - Add Python installation directory
   - Add your project directory

2. **Temporarily disable real-time protection:**
   - Only for testing purposes
   - Re-enable after confirming issue

3. **Use different antivirus software:**
   - Some antivirus software is more aggressive
   - Windows Defender usually works well

## Debugging Tips

### Enable Debug Logging

```python
import logging
logging.basicConfig(level=logging.DEBUG)

# Your agent code here
```

### Test Individual Components

```python
# Test desktop automation
from darbot_windows_agent.desktop import Desktop
desktop = Desktop()
print("Desktop component working")

# Test agent creation
from darbot_windows_agent.agent import Agent
agent = Agent(llm=your_llm)
print("Agent component working")
```

### Monitor System Resources

```python
import psutil
import time

def monitor_resources():
    while True:
        cpu_percent = psutil.cpu_percent()
        memory_percent = psutil.virtual_memory().percent
        print(f"CPU: {cpu_percent}%, Memory: {memory_percent}%")
        time.sleep(5)
```

### Collect Diagnostic Information

```python
import sys
import platform
import pkg_resources

def collect_diagnostic_info():
    print(f"Python version: {sys.version}")
    print(f"Platform: {platform.platform()}")
    print(f"Architecture: {platform.architecture()}")
    
    # List installed packages
    packages = [str(d) for d in pkg_resources.working_set]
    for package in sorted(packages):
        if 'darbot' in package.lower() or 'langchain' in package.lower():
            print(package)

collect_diagnostic_info()
```

## Getting Additional Help

### Before Reporting Issues

1. **Update to latest version:**
   ```bash
   pip install --upgrade darbot-windows-agent
   ```

2. **Try minimal reproduction:**
   - Create simple test case
   - Remove unnecessary complexity

3. **Collect system information:**
   - Python version
   - Windows version
   - Complete error messages
   - Steps to reproduce

### Reporting Issues

When creating a GitHub issue, include:

1. **System Information:**
   - Python version (`python --version`)  
   - Windows version
   - Package version (`pip show darbot-windows-agent`)

2. **Complete Error Messages:**
   - Copy the full traceback
   - Include any warning messages

3. **Reproduction Steps:**
   - Minimal code example
   - Exact steps to reproduce
   - Expected vs actual behavior

4. **Environment Details:**
   - Virtual environment or system installation
   - Other packages installed
   - Any custom configurations

### Community Resources

- **GitHub Issues:** [Report bugs and feature requests](https://github.com/darbotlabs/darbot-windows-agent/issues)
- **Documentation:** Check the main [README](README.md) and [Installation Guide](INSTALLATION.md)
- **Contributing:** See [CONTRIBUTING.md](CONTRIBUTING.md) for development help

This troubleshooting guide covers the most common issues. If you encounter something not covered here, please create an issue on GitHub with detailed information about your problem.