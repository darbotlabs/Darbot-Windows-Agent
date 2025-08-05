<div align="center">

  <h1>🤖 Darbot Windows Agent</h1>
  <a href="https://github.com/darbotlabs/darbot-windows-agent/blob/main/LICENSE">
    <img src="https://img.shields.io/badge/license-MIT-green" alt="License">
  </a>
  <img src="https://img.shields.io/badge/python-3.12%2B-blue" alt="Python">
  <img src="https://img.shields.io/badge/platform-Windows%2010–11-blue" alt="Platform: Windows 10 to 11">
  <img src="https://img.shields.io/github/last-commit/darbotlabs/darbot-windows-agent" alt="Last Commit">

</div>

<br>

**Darbot Windows Agent** is a powerful automation agent that interacts directly with Windows at the GUI layer. It bridges the gap between AI Agents and the Windows OS to perform tasks such as opening apps, clicking buttons, typing, executing shell commands, and capturing UI state—all without relying on traditional computer vision models. This enables any LLM to perform computer automation instead of relying on specific models for it.

## 📋 Table of Contents

- [✨ Key Features](#-key-features)
- [🖥️ Supported Platforms](#️-supported-platforms)
- [🛠️ Installation Guide](#️-installation-guide)
- [⚙️ Basic Usage](#️-basic-usage)
- [🤖 Run Agent](#-run-agent)
- [🎥 Demos](#-demos)
- [📈 Grounding](#-grounding)
- [💡 Vision](#-vision)
- [⚠️ Caution](#️-caution) 
- [🚧 Troubleshooting](#-troubleshooting)
- [🤝 Contributing](#-contributing)
- [🪪 License](#-license)
- [📚 Citation](#-citation)

## ✨ Key Features

• **Native Windows Integration** – Uses UI Automation, Win32 APIs, and PyAutoGUI for reliable control  
• **Zero CV / Vision Optional** – Works with *any* LLM; screenshot attachment is optional  
• **Fast** – Typical end-to-end latency 1.5 – 2.3 seconds per action  
• **Extensible** – Add your own Python tools and automation workflows  
• **LangChain Compatible** – Integrates seamlessly with LangChain agents and workflows  
• **MIT Licensed** – Fork, embed, or commercialize freely

## 🖥️ Supported Platforms

• **Windows 10** (tested)  
• **Windows 11** (recommended)  
• **English Windows locale** (for consistent UI Automation tree)

## 🛠️Installation Guide

### **Prerequisites**

- **Python 3.12 or higher**
- **[UV](https://github.com/astral-sh/uv)** (recommended) or `pip`
- **Windows 10 or 11**
- **English Windows locale** for optimal UI Automation compatibility

### **Installation Steps**

**Install using `uv`:**

```bash
uv pip install darbot-windows-agent
```

Or with pip:

```bash
pip install darbot-windows-agent
```

## ⚙️Basic Usage

```python
# main.py
from langchain_google_genai import ChatGoogleGenerativeAI
from darbot_windows_agent.agent import Agent
from dotenv import load_dotenv

load_dotenv()

llm=ChatGoogleGenerativeAI(model='gemini-2.0-flash')
agent = Agent(llm=llm,browser='chrome',use_vision=True)
query=input("Enter your query: ")
agent_result=agent.invoke(query=query)
print(agent_result.content)
```

## 🤖 Run Agent

You can use the following to run from a script:

```bash
python main.py
Enter your query: <YOUR TASK>
```

---

## 🎥 Demos

**PROMPT:** Write a short note about LLMs and save to the desktop

<https://github.com/user-attachments/assets/0faa5179-73c1-4547-b9e6-2875496b12a0>

**PROMPT:** Change from Dark mode to Light mode

<https://github.com/user-attachments/assets/47bdd166-1261-4155-8890-1b2189c0a3fd>

## 📈 Grounding

![Image](https://github.com/user-attachments/assets/e1d32725-e28a-4821-9c89-24b5ba2e583f)
![Image](https://github.com/user-attachments/assets/be72ad43-c320-4831-95cf-6f1f30df18de)
![Image](https://github.com/user-attachments/assets/d91b513e-13a0-4451-a6e9-f1e16def36e3)
![Image](https://github.com/user-attachments/assets/b5ef5bcf-0e15-4c87-93fe-0f9a983536e5)
![Image](https://github.com/user-attachments/assets/2b5cada6-4ca1-4e0c-8a10-2df29911b1cb)

## 🚧 Troubleshooting

### Common Installation Issues

**Dependency Resolution Error:**
If you encounter dependency conflicts during installation:

```bash
# Try with upgraded pip
python -m pip install --upgrade pip
pip install darbot-windows-agent

# Or use UV for faster dependency resolution
pip install uv
uv pip install darbot-windows-agent
```

**Python Version Issues:**
Ensure you have Python 3.12+ installed:

```bash
python --version
# Should show Python 3.12.x or higher
```

**Import Errors:**
If you encounter import errors, ensure all dependencies are installed:

```bash
pip install langchain langchain-google-genai pyautogui uiautomation
```

### Runtime Issues

**UI Automation Failures:**
- Ensure Windows is set to **English locale**
- Run the agent with **administrator privileges** if needed
- Some applications may require specific timing adjustments

**Agent Not Responding:**
- Check that the LLM API key is properly set in your `.env` file
- Verify network connectivity to the LLM service
- Monitor system resources (CPU/Memory)

For more detailed troubleshooting, please check the [Issues page](https://github.com/darbotlabs/darbot-windows-agent/issues).

## Vision

Talk to your computer. Watch it get things done.

## ⚠️ Caution

Agent interacts directly with your Windows OS at GUI layer to perform actions. While the agent is designed to act intelligently and safely, it can make mistakes that might bring undesired system behaviour or cause unintended changes. Try to run the agent in a sandbox envirnoment.

## 🪪 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🤝 Contributing

Contributions are welcome! Please check the [CONTRIBUTING](CONTRIBUTING.md) file for setup and development workflow.

---

## Citation

```bibtex
@software{
  author       = {Darbot Labs},
  title        = {Darbot Windows Agent: AI-powered Windows automation},
  year         = {2025},
  publisher    = {GitHub},
  url={https://github.com/darbtolabs/darbot-windows-agent}
}
```
