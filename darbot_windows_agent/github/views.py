from pydantic import BaseModel, Field
from typing import Literal, Optional

class GitHubCLI(BaseModel):
    """Schema for GitHub CLI tool operations"""
    command: str = Field(..., description="The GitHub CLI command to execute (without 'gh' prefix)", examples=["auth status", "repo list", "pr list"])
    flags: Optional[str] = Field("", description="Additional flags for the command", examples=["--json", "--limit 10"])

class GitHubModel(BaseModel):
    """Schema for GitHub model selection"""
    provider: Literal['github', 'openai', 'google', 'anthropic', 'groq', 'ollama'] = Field(..., description="The model provider to use")
    model: str = Field(..., description="The specific model name", examples=["gpt-4", "claude-3-sonnet", "gemini-2.0-flash"])
    
class GitHubAuth(BaseModel):
    """Schema for GitHub authentication"""
    action: Literal['login', 'logout', 'status', 'setup-git'] = Field(..., description="Authentication action to perform")
    token: Optional[str] = Field(None, description="GitHub token for authentication (optional)")