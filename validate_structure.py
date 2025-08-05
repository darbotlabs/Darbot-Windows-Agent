#!/usr/bin/env python3
"""
Basic syntax and structure validation for GitHub integration
"""

import ast
import os

def check_file_syntax(filepath):
    """Check if a Python file has valid syntax"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        ast.parse(content)
        return True, None
        
    except SyntaxError as e:
        return False, f"Syntax error: {e}"
    except Exception as e:
        return False, f"Error: {e}"

def check_github_module_structure():
    """Check if GitHub module has correct structure"""
    base_path = "/home/runner/work/Darbot-Windows-Agent/Darbot-Windows-Agent/darbot_windows_agent/github"
    
    required_files = [
        "__init__.py",
        "auth.py", 
        "models.py",
        "views.py",
        "cli.py"
    ]
    
    print("🗂️ Checking GitHub module structure...")
    
    for file in required_files:
        filepath = os.path.join(base_path, file)
        
        if not os.path.exists(filepath):
            print(f"❌ Missing file: {file}")
            return False
        
        is_valid, error = check_file_syntax(filepath)
        if not is_valid:
            print(f"❌ Syntax error in {file}: {error}")
            return False
        
        print(f"✅ {file} - OK")
    
    return True

def check_agent_integration():
    """Check if agent service was properly updated"""
    print("\n🔧 Checking Agent service integration...")
    
    agent_service_path = "/home/runner/work/Darbot-Windows-Agent/Darbot-Windows-Agent/darbot_windows_agent/agent/service.py"
    
    with open(agent_service_path, 'r') as f:
        content = f.read()
    
    checks = [
        ("ModelSelector import", "from darbot_windows_agent.github.models import ModelSelector"),
        ("github_cli_tool import", "github_cli_tool"),
        ("model_selector parameter", "model_selector: ModelSelector"),
        ("GitHub CLI tool in registry", "github_cli_tool")
    ]
    
    for check_name, check_string in checks:
        if check_string in content:
            print(f"✅ {check_name} - Found")
        else:
            print(f"❌ {check_name} - Missing")
            return False
    
    return True

def check_tools_service():
    """Check if tools service has GitHub CLI tool"""
    print("\n🛠️ Checking Tools service...")
    
    tools_service_path = "/home/runner/work/Darbot-Windows-Agent/Darbot-Windows-Agent/darbot_windows_agent/agent/tools/service.py"
    
    with open(tools_service_path, 'r') as f:
        content = f.read()
    
    checks = [
        ("GitHubCLI schema import", "GitHubCLI"),
        ("github_cli_tool function", "def github_cli_tool("),
        ("GitHub CLI @tool decorator", "@tool('GitHub CLI Tool'"),
        ("subprocess import", "import subprocess")
    ]
    
    for check_name, check_string in checks:
        if check_string in content:
            print(f"✅ {check_name} - Found") 
        else:
            print(f"❌ {check_name} - Missing")
            return False
    
    return True

def check_main_enhanced():
    """Check enhanced main file"""
    print("\n🚀 Checking Enhanced main file...")
    
    main_path = "/home/runner/work/Darbot-Windows-Agent/Darbot-Windows-Agent/main_enhanced.py"
    
    if not os.path.exists(main_path):
        print("❌ main_enhanced.py not found")
        return False
    
    is_valid, error = check_file_syntax(main_path)
    if not is_valid:
        print(f"❌ Syntax error in main_enhanced.py: {error}")
        return False
    
    with open(main_path, 'r') as f:
        content = f.read()
    
    checks = [
        ("Model selector menu", "display_model_selector_menu"),
        ("GitHub authentication", "GitHubAuth"),
        ("GitHub Copilot models", "github_copilot"),
        ("Enhanced UI", "GitHub Copilot Integration")
    ]
    
    for check_name, check_string in checks:
        if check_string in content:
            print(f"✅ {check_name} - Found")
        else:
            print(f"❌ {check_name} - Missing")
            return False
    
    print("✅ main_enhanced.py - OK")
    return True

def main():
    """Run all structure checks"""
    print("🔍 GitHub CLI and Model Selection - Structure Validation")
    print("=" * 60)
    
    checks = [
        check_github_module_structure,
        check_agent_integration,
        check_tools_service,
        check_main_enhanced
    ]
    
    passed = 0
    for check in checks:
        if check():
            passed += 1
            print()
    
    print("=" * 60)
    print(f"📊 Structure Check Results: {passed}/{len(checks)} checks passed")
    
    if passed == len(checks):
        print("🎉 All structure checks completed successfully!")
        print("💡 The integration is ready for testing with proper dependencies.")
        return 0
    else:
        print(f"⚠️  {len(checks) - passed} check(s) failed")
        return 1

if __name__ == "__main__":
    exit(main())