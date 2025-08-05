import unittest
from unittest.mock import patch, MagicMock
import sys
import os

# Add the project root to the Python path
sys.path.insert(0, '/home/runner/work/Darbot-Windows-Agent/Darbot-Windows-Agent')

class TestGitHubIntegration(unittest.TestCase):
    """Test GitHub CLI and model selection integration"""

    def test_github_models_module_structure(self):
        """Test that the GitHub models module has expected structure"""
        # This test doesn't require external dependencies
        import ast
        
        models_path = '/home/runner/work/Darbot-Windows-Agent/Darbot-Windows-Agent/darbot_windows_agent/github/models.py'
        
        with open(models_path, 'r') as f:
            content = f.read()
        
        # Check that the file parses correctly
        tree = ast.parse(content)
        
        # Find class definitions
        class_names = [node.name for node in ast.walk(tree) if isinstance(node, ast.ClassDef)]
        
        self.assertIn('ModelSelector', class_names)
        self.assertIn('ModelConfig', class_names)

    def test_github_auth_module_structure(self):
        """Test that the GitHub auth module has expected structure"""
        import ast
        
        auth_path = '/home/runner/work/Darbot-Windows-Agent/Darbot-Windows-Agent/darbot_windows_agent/github/auth.py'
        
        with open(auth_path, 'r') as f:
            content = f.read()
        
        # Check that the file parses correctly
        tree = ast.parse(content)
        
        # Find class definitions
        class_names = [node.name for node in ast.walk(tree) if isinstance(node, ast.ClassDef)]
        function_names = [node.name for node in ast.walk(tree) if isinstance(node, ast.FunctionDef)]
        
        self.assertIn('GitHubAuth', class_names)
        self.assertIn('github_cli_tool', function_names)

    def test_tools_service_has_github_cli(self):
        """Test that tools service includes GitHub CLI tool"""
        tools_service_path = '/home/runner/work/Darbot-Windows-Agent/Darbot-Windows-Agent/darbot_windows_agent/agent/tools/service.py'
        
        with open(tools_service_path, 'r') as f:
            content = f.read()
        
        # Check for GitHub CLI tool function
        self.assertIn('def github_cli_tool(', content)
        self.assertIn("@tool('GitHub CLI Tool'", content)
        self.assertIn('subprocess', content)

    def test_agent_service_integration(self):
        """Test that agent service has been updated for GitHub integration"""
        agent_service_path = '/home/runner/work/Darbot-Windows-Agent/Darbot-Windows-Agent/darbot_windows_agent/agent/service.py'
        
        with open(agent_service_path, 'r') as f:
            content = f.read()
        
        # Check for model selector integration
        self.assertIn('ModelSelector', content)
        self.assertIn('github_cli_tool', content)
        self.assertIn('model_selector:', content)

    def test_enhanced_main_structure(self):
        """Test that enhanced main has correct structure"""
        main_path = '/home/runner/work/Darbot-Windows-Agent/Darbot-Windows-Agent/main_enhanced.py'
        
        self.assertTrue(os.path.exists(main_path))
        
        with open(main_path, 'r') as f:
            content = f.read()
        
        # Check for key functionality
        self.assertIn('display_model_selector_menu', content)
        self.assertIn('setup_llm_from_selection', content)
        self.assertIn('GitHub Copilot', content)
        self.assertIn('ModelSelector', content)

    @unittest.skip("Requires pydantic and other dependencies")
    def test_github_cli_tool_execution(self):
        """Test GitHub CLI tool execution (mocked)"""
        # Mock subprocess.run for GitHub CLI check
        mock_result = MagicMock()
        mock_result.returncode = 0
        mock_result.stdout = "gh version 2.40.0"
        mock_result.stderr = ""
        
        with patch('subprocess.run', return_value=mock_result):
            # Import here to avoid dependency issues in CI
            from darbot_windows_agent.agent.tools.service import github_cli_tool
            
            result = github_cli_tool("--version")
            self.assertIn("Command executed successfully", result)
            self.assertIn("gh version", result)

    def test_model_config_structure(self):
        """Test ModelConfig dataclass structure"""
        import ast
        
        models_path = '/home/runner/work/Darbot-Windows-Agent/Darbot-Windows-Agent/darbot_windows_agent/github/models.py'
        
        with open(models_path, 'r') as f:
            content = f.read()
        
        # Check for model configurations
        self.assertIn('gpt-4', content)
        self.assertIn('gemini-2.0-flash', content)
        self.assertIn('github_copilot', content)
        self.assertIn('AVAILABLE_MODELS', content)

if __name__ == '__main__':
    unittest.main()