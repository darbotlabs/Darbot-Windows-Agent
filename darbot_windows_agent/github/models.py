import os
import json
from typing import Dict, List, Optional, Any
from dataclasses import dataclass
from langchain_core.language_models.chat_models import BaseChatModel
from langchain_openai import ChatOpenAI
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_groq import ChatGroq
from langchain_ollama import ChatOllama
from darbot_windows_agent.github.auth import GitHubAuth

@dataclass
class ModelConfig:
    """Configuration for a language model"""
    name: str
    display_name: str
    provider: str
    requires_api_key: bool
    api_key_env: Optional[str] = None
    default_params: Optional[Dict[str, Any]] = None

class ModelSelector:
    """Manages model selection similar to VSCode GitHub Copilot"""
    
    # Available models with their configurations
    AVAILABLE_MODELS = {
        # GitHub Copilot models (requires GitHub authentication)
        "gpt-4": ModelConfig(
            name="gpt-4",
            display_name="GPT-4 (GitHub Copilot)",
            provider="github_copilot",
            requires_api_key=False,  # Uses GitHub token
        ),
        "gpt-4-turbo": ModelConfig(
            name="gpt-4-turbo",
            display_name="GPT-4 Turbo (GitHub Copilot)",
            provider="github_copilot", 
            requires_api_key=False,
        ),
        "gpt-3.5-turbo": ModelConfig(
            name="gpt-3.5-turbo",
            display_name="GPT-3.5 Turbo (GitHub Copilot)",
            provider="github_copilot",
            requires_api_key=False,
        ),
        
        # Direct OpenAI models
        "openai-gpt-4": ModelConfig(
            name="gpt-4",
            display_name="GPT-4 (Direct OpenAI)",
            provider="openai",
            requires_api_key=True,
            api_key_env="OPENAI_API_KEY"
        ),
        "openai-gpt-4-turbo": ModelConfig(
            name="gpt-4-turbo",
            display_name="GPT-4 Turbo (Direct OpenAI)",
            provider="openai",
            requires_api_key=True,
            api_key_env="OPENAI_API_KEY"
        ),
        "openai-gpt-3.5-turbo": ModelConfig(
            name="gpt-3.5-turbo",
            display_name="GPT-3.5 Turbo (Direct OpenAI)",
            provider="openai",
            requires_api_key=True,
            api_key_env="OPENAI_API_KEY"
        ),
        
        # Google models
        "gemini-2.0-flash": ModelConfig(
            name="gemini-2.0-flash",
            display_name="Gemini 2.0 Flash",
            provider="google",
            requires_api_key=True,
            api_key_env="GOOGLE_API_KEY"
        ),
        "gemini-1.5-pro": ModelConfig(
            name="gemini-1.5-pro",
            display_name="Gemini 1.5 Pro",
            provider="google",
            requires_api_key=True,
            api_key_env="GOOGLE_API_KEY"
        ),
        
        # Groq models
        "groq-llama3-70b": ModelConfig(
            name="llama-3.1-70b-versatile",
            display_name="Llama 3.1 70B (Groq)",
            provider="groq",
            requires_api_key=True,
            api_key_env="GROQ_API_KEY"
        ),
        "groq-mixtral": ModelConfig(
            name="mixtral-8x7b-32768",
            display_name="Mixtral 8x7B (Groq)",
            provider="groq",
            requires_api_key=True,
            api_key_env="GROQ_API_KEY"
        ),
        
        # Ollama models (local)
        "ollama-llama3": ModelConfig(
            name="llama3",
            display_name="Llama 3 (Local Ollama)",
            provider="ollama",
            requires_api_key=False
        ),
        "ollama-codellama": ModelConfig(
            name="codellama",
            display_name="Code Llama (Local Ollama)",
            provider="ollama",
            requires_api_key=False
        ),
    }
    
    def __init__(self):
        self.selected_model: Optional[str] = None
        self.github_auth = GitHubAuth()
    
    def list_available_models(self) -> List[Dict[str, Any]]:
        """List all available models with their status"""
        models = []
        
        for model_id, config in self.AVAILABLE_MODELS.items():
            model_info = {
                "id": model_id,
                "name": config.display_name,
                "provider": config.provider,
                "available": self._is_model_available(config)
            }
            
            if not model_info["available"]:
                model_info["reason"] = self._get_unavailable_reason(config)
            
            models.append(model_info)
        
        return models
    
    def _is_model_available(self, config: ModelConfig) -> bool:
        """Check if a model is available for use"""
        if config.provider == "github_copilot":
            return self.github_auth.is_authenticated()
        elif config.requires_api_key and config.api_key_env:
            return bool(os.getenv(config.api_key_env))
        else:
            return True  # Ollama or other local models
    
    def _get_unavailable_reason(self, config: ModelConfig) -> str:
        """Get reason why a model is unavailable"""
        if config.provider == "github_copilot":
            return "GitHub authentication required"
        elif config.requires_api_key and config.api_key_env:
            return f"API key required: {config.api_key_env}"
        else:
            return "Unknown issue"
    
    def select_model(self, model_id: str) -> bool:
        """Select a model for use"""
        if model_id not in self.AVAILABLE_MODELS:
            return False
        
        config = self.AVAILABLE_MODELS[model_id]
        if not self._is_model_available(config):
            return False
        
        self.selected_model = model_id
        return True
    
    def get_selected_model(self) -> Optional[str]:
        """Get currently selected model"""
        return self.selected_model
    
    def create_llm(self, model_id: Optional[str] = None) -> Optional[BaseChatModel]:
        """Create LLM instance for the specified or selected model"""
        target_model = model_id or self.selected_model
        
        if not target_model or target_model not in self.AVAILABLE_MODELS:
            return None
        
        config = self.AVAILABLE_MODELS[target_model]
        
        if not self._is_model_available(config):
            return None
        
        try:
            if config.provider == "github_copilot":
                # Use GitHub token for authentication with OpenAI
                github_token = self.github_auth.get_token()
                if not github_token:
                    return None
                
                return ChatOpenAI(
                    model=config.name,
                    api_key=github_token,
                    base_url="https://models.inference.ai.azure.com"  # GitHub Copilot endpoint
                )
            
            elif config.provider == "openai":
                api_key = os.getenv(config.api_key_env)
                if not api_key:
                    return None
                return ChatOpenAI(model=config.name, api_key=api_key)
            
            elif config.provider == "google":
                api_key = os.getenv(config.api_key_env)
                if not api_key:
                    return None
                return ChatGoogleGenerativeAI(model=config.name, google_api_key=api_key)
            
            elif config.provider == "groq":
                api_key = os.getenv(config.api_key_env)
                if not api_key:
                    return None
                return ChatGroq(model=config.name, groq_api_key=api_key)
            
            elif config.provider == "ollama":
                return ChatOllama(model=config.name)
            
        except Exception as e:
            print(f"Error creating LLM for {target_model}: {e}")
            return None
        
        return None
    
    def get_model_info(self, model_id: str) -> Optional[Dict[str, Any]]:
        """Get detailed information about a specific model"""
        if model_id not in self.AVAILABLE_MODELS:
            return None
        
        config = self.AVAILABLE_MODELS[model_id]
        return {
            "id": model_id,
            "name": config.display_name,
            "provider": config.provider,
            "requires_api_key": config.requires_api_key,
            "api_key_env": config.api_key_env,
            "available": self._is_model_available(config),
            "reason": self._get_unavailable_reason(config) if not self._is_model_available(config) else None
        }