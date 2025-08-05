import subprocess
import json
import os
from typing import Tuple
from darbot_windows_agent.github.views import GitHubCLI
from darbot_windows_agent.desktop import Desktop
from langchain.tools import tool

class GitHubAuth:
    """GitHub authentication management"""
    
    @staticmethod
    def is_authenticated() -> bool:
        """Check if user is authenticated with GitHub CLI"""
        try:
            result = subprocess.run(
                ["gh", "auth", "status"], 
                capture_output=True, 
                text=True, 
                timeout=30
            )
            return result.returncode == 0
        except (subprocess.TimeoutExpired, FileNotFoundError):
            return False
    
    @staticmethod
    def login() -> Tuple[str, bool]:
        """Initiate GitHub CLI login process"""
        try:
            result = subprocess.run(
                ["gh", "auth", "login", "--web"], 
                capture_output=True, 
                text=True, 
                timeout=300
            )
            if result.returncode == 0:
                return "Successfully authenticated with GitHub CLI", True
            else:
                return f"Authentication failed: {result.stderr}", False
        except subprocess.TimeoutExpired:
            return "Authentication timed out", False
        except FileNotFoundError:
            return "GitHub CLI not found. Please install it from https://cli.github.com/", False
    
    @staticmethod 
    def status() -> str:
        """Get GitHub authentication status"""
        try:
            result = subprocess.run(
                ["gh", "auth", "status"], 
                capture_output=True, 
                text=True, 
                timeout=30
            )
            return result.stdout if result.returncode == 0 else result.stderr
        except (subprocess.TimeoutExpired, FileNotFoundError):
            return "GitHub CLI not available or not authenticated"
    
    @staticmethod
    def get_token() -> str:
        """Get GitHub token if available"""
        try:
            result = subprocess.run(
                ["gh", "auth", "token"], 
                capture_output=True, 
                text=True, 
                timeout=30
            )
            return result.stdout.strip() if result.returncode == 0 else ""
        except (subprocess.TimeoutExpired, FileNotFoundError):
            return ""

@tool('GitHub CLI Tool', args_schema=GitHubCLI)
def github_cli_tool(command: str, flags: str = "", desktop: Desktop = None) -> str:
    """Execute GitHub CLI commands for repository management, issue tracking, PR management, etc.
    
    Examples:
    - "auth status" - Check authentication status
    - "repo list" - List repositories
    - "pr list" - List pull requests
    - "issue list" - List issues
    - "repo view" - View repository details
    """
    
    # Check if GitHub CLI is installed
    try:
        subprocess.run(["gh", "--version"], capture_output=True, timeout=10)
    except (subprocess.TimeoutExpired, FileNotFoundError):
        return "GitHub CLI is not installed. Please install it from https://cli.github.com/"
    
    # Build the full command
    full_command = ["gh"] + command.split()
    if flags:
        full_command.extend(flags.split())
    
    try:
        result = subprocess.run(
            full_command,
            capture_output=True,
            text=True,
            timeout=60
        )
        
        if result.returncode == 0:
            return f"Command executed successfully:\n{result.stdout}"
        else:
            error_msg = result.stderr or "Unknown error occurred"
            if "not authenticated" in error_msg.lower():
                return f"Authentication required. Please run GitHub CLI authentication first.\nError: {error_msg}"
            return f"Command failed with exit code {result.returncode}:\n{error_msg}"
            
    except subprocess.TimeoutExpired:
        return f"Command timed out: gh {command} {flags}"
    except Exception as e:
        return f"Error executing GitHub CLI command: {str(e)}"