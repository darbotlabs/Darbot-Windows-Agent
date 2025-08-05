# 👨‍💻 Development Guide - Darbot Windows Agent

<div align="center">
  <h2>👨‍💻 Development Guide</h2>
</div>

This comprehensive guide covers development setup, contributing code, testing, and understanding the project architecture.

## 📋 Table of Contents

- [Development Environment Setup](#development-environment-setup)
- [Project Architecture](#project-architecture)
- [Adding New Features](#adding-new-features)
- [Testing](#testing)
- [Code Standards](#code-standards)
- [Debugging](#debugging)
- [Release Process](#release-process)

## Development Environment Setup

### Prerequisites

- **Windows 10/11** (primary development platform)
- **Python 3.12+** with pip
- **Git** for version control
- **VS Code** (recommended) or your preferred IDE

### Initial Setup

1. **Fork and clone the repository:**
   ```bash
   git clone https://github.com/yourusername/darbot-windows-agent.git
   cd darbot-windows-agent
   ```

2. **Create development environment:**

   **Option A: Using virtual environment (recommended)**
   ```bash
   python -m venv venv
   venv\Scripts\activate
   pip install -e .[dev]
   ```

   **Option B: Using UV (faster)**
   ```bash
   pip install uv
   uv venv
   .venv\Scripts\activate
   uv pip install -e .[dev]
   ```

3. **Set up pre-commit hooks (optional):**
   ```bash
   pip install pre-commit
   pre-commit install
   ```

4. **Create development configuration:**
   ```bash
   # Copy example environment file
   copy .env-example .env
   # Edit .env with your API keys
   ```

## Project Architecture

### Directory Structure

```
darbot-windows-agent/
├── darbot_windows_agent/          # Main package
│   ├── __init__.py               # Package initialization
│   ├── agent/                    # Agent implementation
│   │   ├── __init__.py
│   │   ├── service.py           # Main agent service
│   │   ├── views.py             # Agent views/interfaces
│   │   ├── utils.py             # Agent utilities
│   │   ├── prompt/              # Prompt engineering
│   │   │   └── service.py
│   │   ├── registry/            # Component registry
│   │   └── tools/               # Agent tools
│   │       ├── service.py       # Tools service
│   │       └── views.py         # Tools interface
│   ├── desktop/                  # Desktop automation
│   │   ├── __init__.py
│   │   ├── config.py            # Desktop configuration
│   │   └── views.py             # Desktop interface
│   └── tree/                     # UI tree representation
│       └── __init__.py
├── tests/                        # Test suite
│   ├── __init__.py
│   └── unit/                     # Unit tests
│       ├── agent/               # Agent tests
│       ├── desktop/             # Desktop tests
│       └── tree/                # Tree tests
├── static/                       # Static assets
├── main.py                       # Main entry point
├── pyproject.toml               # Project configuration
├── README.md                    # Main documentation
├── CONTRIBUTING.md              # Contribution guidelines
├── INSTALLATION.md              # Installation guide
├── TROUBLESHOOTING.md           # Troubleshooting guide
└── DEVELOPMENT.md               # This file
```

### Key Components

#### Agent Module (`darbot_windows_agent/agent/`)
- **service.py**: Core agent logic and LLM integration
- **views.py**: Agent interface and response handling
- **tools/**: Available tools for desktop automation
- **prompt/**: Prompt engineering and templates

#### Desktop Module (`darbot_windows_agent/desktop/`)
- **views.py**: Desktop class with Windows automation methods
- **config.py**: Configuration for desktop automation

#### Tree Module (`darbot_windows_agent/tree/`)
- UI element tree representation and navigation

### Architecture Patterns

The project follows several key patterns:

1. **Service Layer Pattern**: Business logic separated from presentation
2. **Repository Pattern**: Data access abstraction
3. **Command Pattern**: Actions encapsulated as objects
4. **Observer Pattern**: Event-driven updates

## Adding New Features

### Agent Tools

To add a new agent tool:

1. **Create tool function** in `darbot_windows_agent/agent/tools/views.py`:

```python
def new_automation_tool(self, parameter: str) -> str:
    """
    New automation tool description.
    
    Args:
        parameter: Description of parameter
        
    Returns:
        str: Result message
    """
    try:
        # Implementation logic
        result = self.desktop.some_method(parameter)
        return f"Success: {result}"
    except Exception as e:
        return f"Error: {str(e)}"
```

2. **Register tool** in the tools service:

```python
# In darbot_windows_agent/agent/tools/service.py
def get_available_tools(self):
    tools = [
        # ... existing tools
        {
            'name': 'new_automation_tool',
            'description': 'Description of new tool',
            'function': self.views.new_automation_tool
        }
    ]
    return tools
```

3. **Add tests** in `tests/unit/agent/agent_tools/`:

```python
def test_new_automation_tool():
    agent_tools = AgentTools()
    result = agent_tools.new_automation_tool("test_parameter")
    assert "Success" in result or "Error" in result
```

### Desktop Automation Methods

To add new desktop automation capabilities:

1. **Add method** to `darbot_windows_agent/desktop/views.py`:

```python
def new_desktop_method(self, parameter: str) -> tuple[str, int]:
    """
    New desktop automation method.
    
    Args:
        parameter: Method parameter
        
    Returns:
        tuple: (result_message, status_code)
    """
    try:
        # Use pyautogui, uiautomation, or Windows APIs
        import pyautogui as pg
        import uiautomation as ua
        
        # Implementation
        result = "Method executed successfully"
        return (result, 0)
    except Exception as e:
        return (f"Error: {str(e)}", 1)
```

2. **Add configuration** if needed in `darbot_windows_agent/desktop/config.py`

3. **Write tests** in `tests/unit/desktop/`

### UI Tree Extensions

To extend UI tree functionality:

1. **Add methods** to tree module
2. **Update tree parsing logic**
3. **Add integration with desktop automation**

## Testing

### Running Tests

```bash
# Run all tests
python -m pytest tests/ -v

# Run specific test module
python -m pytest tests/unit/agent/ -v

# Run with coverage
python -m pytest tests/ --cov=darbot_windows_agent --cov-report=html
```

### Test Structure

Tests are organized by component:

```
tests/
├── unit/
│   ├── agent/
│   │   ├── test_agent_service.py
│   │   ├── test_agent_views.py
│   │   ├── test_agent_utils.py
│   │   └── agent_tools/
│   ├── desktop/
│   │   ├── test_desktop_views.py
│   │   └── test_desktop_config.py
│   └── tree/
│       └── test_tree_operations.py
└── integration/  # Integration tests (optional)
```

### Writing Tests

#### Unit Test Example

```python
import pytest
from darbot_windows_agent.agent.service import AgentService
from darbot_windows_agent.desktop.views import Desktop

class TestAgentService:
    def setup_method(self):
        """Set up test fixtures."""
        self.desktop = Desktop()
        self.agent_service = AgentService()
    
    def test_agent_initialization(self):
        """Test agent initialization."""
        assert self.agent_service is not None
        assert hasattr(self.agent_service, 'desktop')
    
    def test_agent_query_processing(self):
        """Test query processing."""
        query = "Test query"
        result = self.agent_service.process_query(query)
        assert isinstance(result, str)
        assert len(result) > 0
```

#### Mock External Dependencies

```python
from unittest.mock import Mock, patch

@patch('darbot_windows_agent.desktop.views.pyautogui')
def test_desktop_click(mock_pyautogui):
    """Test desktop click with mocked pyautogui."""
    mock_pyautogui.click.return_value = None
    
    desktop = Desktop()
    result, status = desktop.click_at_position(100, 100)
    
    mock_pyautogui.click.assert_called_once_with(100, 100)
    assert status == 0
```

### Testing Guidelines

1. **Write tests for new features**: Every new function should have tests
2. **Use meaningful test names**: Clearly describe what is being tested
3. **Test edge cases**: Include error conditions and boundary values
4. **Mock external dependencies**: UI automation, API calls, file system
5. **Keep tests independent**: Each test should run in isolation

## Code Standards

### Python Style Guide

Follow PEP 8 and project conventions:

```python
# Good: Clear function names and docstrings
def process_desktop_automation(self, action_type: str, parameters: dict) -> str:
    """
    Process desktop automation request.
    
    Args:
        action_type: Type of automation action
        parameters: Action parameters
        
    Returns:
        str: Result message
        
    Raises:
        ValueError: If action_type is invalid
    """
    if not action_type:
        raise ValueError("Action type cannot be empty")
    
    # Implementation
    return "Action completed successfully"

# Good: Type hints and error handling
def safe_ui_operation(element_name: str) -> tuple[bool, str]:
    """Safely perform UI operation with proper error handling."""
    try:
        # UI operation logic
        return (True, "Operation successful")
    except Exception as e:
        logger.error(f"UI operation failed: {e}")
        return (False, f"Error: {str(e)}")
```

### Code Organization

1. **Imports**: Standard library, third-party, local imports
2. **Constants**: Define at module level
3. **Classes**: One primary class per file
4. **Functions**: Logical grouping within classes
5. **Error Handling**: Comprehensive exception handling

### Documentation Standards

1. **Docstrings**: Use Google-style docstrings
2. **Type Hints**: Include for all function parameters and returns
3. **Comments**: Explain complex logic, not obvious code
4. **README Updates**: Update documentation for new features

## Debugging

### Development Debugging

```python
# Enable debug logging
import logging
logging.basicConfig(level=logging.DEBUG)

# Add debug prints in development
logger = logging.getLogger(__name__)
logger.debug(f"Processing query: {query}")
```

### VS Code Debugging

1. **Configure launch.json**:
```json
{
    "version": "0.2.0",
    "configurations": [
        {
            "name": "Debug Agent",
            "type": "python",
            "request": "launch",
            "program": "${workspaceFolder}/main.py",
            "console": "integratedTerminal",
            "cwd": "${workspaceFolder}"
        }
    ]
}
```

2. **Set breakpoints** in VS Code
3. **Use debug console** for interactive debugging

### Performance Profiling

```python
import cProfile
import pstats

def profile_agent_performance():
    """Profile agent performance."""
    profiler = cProfile.Profile()
    profiler.enable()
    
    # Agent operations here
    agent.invoke("test query")
    
    profiler.disable()
    stats = pstats.Stats(profiler)
    stats.sort_stats('cumulative')
    stats.print_stats(10)  # Top 10 functions
```

### Common Debugging Scenarios

1. **UI Automation Issues**: Use Windows Inspect tool
2. **LLM Integration**: Check API responses and rate limits
3. **Performance**: Profile code and check system resources
4. **Memory Leaks**: Monitor memory usage over time

## Release Process

### Pre-Release Checklist

- [ ] All tests pass
- [ ] Documentation updated
- [ ] Version numbers consistent
- [ ] Changelog updated
- [ ] No breaking changes (or properly documented)

### Version Management

Update version in `pyproject.toml`:

```toml
[project]
name = "darbot-windows-agent"
version = "0.6.0"  # Update this
```

### Release Steps

1. **Create release branch:**
   ```bash
   git checkout -b release/v0.6.0
   ```

2. **Update version and changelog:**
   ```bash
   # Update pyproject.toml
   # Update CHANGELOG.md
   ```

3. **Run full test suite:**
   ```bash
   python -m pytest tests/ --cov=darbot_windows_agent
   ```

4. **Create pull request** for release branch

5. **After merge, tag release:**
   ```bash
   git tag v0.6.0
   git push origin v0.6.0
   ```

6. **Build and publish** (if applicable):
   ```bash
   python -m build
   python -m twine upload dist/*
   ```

### Hotfix Process

For critical bug fixes:

1. **Create hotfix branch** from main
2. **Apply minimal fix**
3. **Test thoroughly** 
4. **Fast-track review**
5. **Deploy immediately**

## Contributing Workflow

1. **Fork repository** on GitHub
2. **Create feature branch**: `git checkout -b feature/new-feature`
3. **Make changes** following code standards
4. **Write/update tests**
5. **Update documentation**
6. **Commit changes**: Use conventional commit messages
7. **Push to fork**: `git push origin feature/new-feature`
8. **Create pull request** with detailed description

### Commit Message Format

```
type(scope): brief description

Detailed description if needed

- Breaking changes noted
- Issue references: Fixes #123
```

Types: `feat`, `fix`, `docs`, `test`, `refactor`, `chore`

This development guide provides the foundation for contributing to Darbot Windows Agent. For specific contribution guidelines, see [CONTRIBUTING.md](CONTRIBUTING.md).

For installation help, see [INSTALLATION.md](INSTALLATION.md).
For troubleshooting, see [TROUBLESHOOTING.md](TROUBLESHOOTING.md).