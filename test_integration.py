#!/usr/bin/env python3
"""
Test script for GitHub CLI and Model Selection integration
"""

import sys
import os

# Add the project root to the Python path
sys.path.insert(0, '/home/runner/work/Darbot-Windows-Agent/Darbot-Windows-Agent')

def test_github_cli_tool():
    """Test the GitHub CLI tool"""
    print("🧪 Testing GitHub CLI Tool...")
    
    try:
        from darbot_windows_agent.agent.tools.service import github_cli_tool
        
        # Test basic GitHub CLI availability
        result = github_cli_tool("--version")
        print(f"✅ GitHub CLI tool imported and executed:")
        print(f"   Result: {result[:100]}..." if len(result) > 100 else f"   Result: {result}")
        return True
        
    except Exception as e:
        print(f"❌ GitHub CLI tool test failed: {e}")
        return False

def test_model_selector():
    """Test the model selector"""
    print("\n🧪 Testing Model Selector...")
    
    try:
        from darbot_windows_agent.github.models import ModelSelector
        
        model_selector = ModelSelector()
        available_models = model_selector.list_available_models()
        
        print(f"✅ Model selector imported successfully")
        print(f"   Found {len(available_models)} models:")
        
        for model in available_models[:3]:  # Show first 3 models
            status = "✅" if model['available'] else "❌"
            print(f"   {status} {model['name']} ({model['provider']})")
        
        if len(available_models) > 3:
            print(f"   ... and {len(available_models) - 3} more")
        
        return True
        
    except Exception as e:
        print(f"❌ Model selector test failed: {e}")
        return False

def test_github_auth():
    """Test GitHub authentication"""
    print("\n🧪 Testing GitHub Authentication...")
    
    try:
        from darbot_windows_agent.github.auth import GitHubAuth
        
        github_auth = GitHubAuth()
        is_authenticated = github_auth.is_authenticated()
        status = github_auth.status()
        
        print(f"✅ GitHub auth imported successfully")
        print(f"   Authenticated: {'Yes' if is_authenticated else 'No'}")
        print(f"   Status: {status[:100]}..." if len(status) > 100 else f"   Status: {status}")
        
        return True
        
    except Exception as e:
        print(f"❌ GitHub auth test failed: {e}")
        return False

def test_agent_integration():
    """Test Agent integration with new components"""
    print("\n🧪 Testing Agent Integration...")
    
    try:
        from darbot_windows_agent.agent import Agent
        from darbot_windows_agent.github.models import ModelSelector
        
        # Create a mock LLM for testing
        class MockLLM:
            def invoke(self, messages):
                return type('MockMessage', (), {'content': 'Mock response'})()
        
        model_selector = ModelSelector()
        agent = Agent(llm=MockLLM(), model_selector=model_selector, use_vision=False)
        
        print(f"✅ Agent integration successful")
        print(f"   Agent name: {agent.name}")
        print(f"   Model selector available: {agent.model_selector is not None}")
        print(f"   Tools count: {len(agent.registry.tools)}")
        
        # Check if GitHub CLI tool is in the registry
        tool_names = [tool.name for tool in agent.registry.tools]
        github_tool_present = any('github' in name.lower() for name in tool_names)
        print(f"   GitHub CLI tool present: {'Yes' if github_tool_present else 'No'}")
        
        return True
        
    except Exception as e:
        print(f"❌ Agent integration test failed: {e}")
        return False

def main():
    """Run all tests"""
    print("🚀 Running GitHub CLI and Model Selection Integration Tests")
    print("=" * 60)
    
    tests = [
        test_github_cli_tool,
        test_model_selector, 
        test_github_auth,
        test_agent_integration
    ]
    
    passed = 0
    for test in tests:
        if test():
            passed += 1
    
    print("\n" + "=" * 60)
    print(f"📊 Test Results: {passed}/{len(tests)} tests passed")
    
    if passed == len(tests):
        print("🎉 All tests completed successfully!")
        return 0
    else:
        print(f"⚠️  {len(tests) - passed} test(s) failed")
        return 1

if __name__ == "__main__":
    sys.exit(main())