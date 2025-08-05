import os
import sys
from typing import Optional

# Handle optional dotenv import
try:
    from dotenv import load_dotenv
    DOTENV_AVAILABLE = True
except ImportError:
    DOTENV_AVAILABLE = False
    load_dotenv = lambda: None

def check_dependencies():
    """Check if required dependencies are available."""
    missing_deps = []
    
    try:
        import langchain
    except ImportError:
        missing_deps.append("langchain")
    
    try:
        from darbot_windows_agent.agent import Agent
    except ImportError:
        missing_deps.append("darbot-windows-agent (agent module)")
    
    try:
        from darbot_windows_agent.github.models import ModelSelector
        from darbot_windows_agent.github.auth import GitHubAuth
    except ImportError:
        missing_deps.append("darbot-windows-agent (github modules)")
    
    if missing_deps:
        print("❌ Missing required dependencies:")
        for dep in missing_deps:
            print(f"   - {dep}")
        print("\n💡 Please install dependencies:")
        print("   pip install darbot-windows-agent")
        return False
    
    return True

def display_model_selector_menu():
    """Display interactive model selection menu"""
    from darbot_windows_agent.github.models import ModelSelector
    from darbot_windows_agent.github.auth import GitHubAuth
    
    model_selector = ModelSelector()
    github_auth = GitHubAuth()
    
    print("\n🤖 Available Language Models:")
    print("=" * 50)
    
    models = model_selector.list_available_models()
    
    # Group models by provider
    providers = {}
    for idx, model in enumerate(models, 1):
        provider = model['provider']
        if provider not in providers:
            providers[provider] = []
        providers[provider].append((idx, model))
    
    # Display grouped models
    for provider, provider_models in providers.items():
        provider_name = {
            'github_copilot': '🔗 GitHub Copilot',
            'openai': '🚀 OpenAI (Direct)',
            'google': '🔍 Google AI',
            'groq': '⚡ Groq',
            'ollama': '🏠 Ollama (Local)'
        }.get(provider, provider.title())
        
        print(f"\n{provider_name}:")
        for idx, model in provider_models:
            status = "✅" if model['available'] else "❌"
            print(f"  {idx}. {status} {model['name']}")
            if not model['available']:
                print(f"     └─ {model.get('reason', 'Unavailable')}")
    
    print(f"\n{len(models) + 1}. 🔧 Setup GitHub Authentication")
    print(f"{len(models) + 2}. ❓ GitHub Authentication Status")
    print(f"{len(models) + 3}. 🔙 Continue without model selection")
    
    while True:
        try:
            choice = input(f"\nSelect a model (1-{len(models) + 3}): ").strip()
            
            if not choice:
                continue
                
            choice_num = int(choice)
            
            if choice_num == len(models) + 1:
                # Setup GitHub Authentication
                print("\n🔧 Setting up GitHub Authentication...")
                result, success = github_auth.login()
                print(result)
                if success:
                    print("✅ GitHub authentication successful!")
                    print("💡 GitHub Copilot models are now available.")
                continue
            
            elif choice_num == len(models) + 2:
                # Show GitHub status
                print("\n📊 GitHub Authentication Status:")
                status = github_auth.status()
                print(status)
                continue
            
            elif choice_num == len(models) + 3:
                # Continue without selection
                return None, model_selector
            
            elif 1 <= choice_num <= len(models):
                selected_model = models[choice_num - 1]
                
                if not selected_model['available']:
                    print(f"❌ Model '{selected_model['name']}' is not available.")
                    print(f"   Reason: {selected_model.get('reason', 'Unknown')}")
                    continue
                
                model_id = selected_model['id']
                if model_selector.select_model(model_id):
                    print(f"✅ Selected model: {selected_model['name']}")
                    return model_id, model_selector
                else:
                    print(f"❌ Failed to select model: {selected_model['name']}")
                    continue
            else:
                print(f"❌ Invalid choice. Please enter a number between 1 and {len(models) + 3}.")
                
        except ValueError:
            print("❌ Invalid input. Please enter a number.")
        except KeyboardInterrupt:
            print("\n👋 Model selection cancelled.")
            return None, model_selector

def setup_llm_from_selection(model_id: Optional[str], model_selector):
    """Setup LLM based on model selection"""
    if model_id:
        print(f"🔄 Initializing {model_id}...")
        llm = model_selector.create_llm(model_id)
        if llm:
            print("✅ LLM initialized successfully")
            return llm
        else:
            print("❌ Failed to initialize selected model, falling back to default")
    
    # Fallback to default behavior
    print("🔄 Trying fallback models...")
    
    # Try Google Gemini as default
    if DOTENV_AVAILABLE:
        load_dotenv()
    
    google_api_key = os.getenv("GOOGLE_API_KEY")
    if google_api_key:
        try:
            from langchain_google_genai import ChatGoogleGenerativeAI
            llm = ChatGoogleGenerativeAI(model='gemini-2.0-flash')
            print("✅ Using Google Gemini as fallback")
            return llm
        except Exception as e:
            print(f"❌ Failed to initialize Gemini: {e}")
    
    print("❌ No available models found. Please set up at least one API key or GitHub authentication.")
    return None

def main():
    """Main entry point for the Darbot Windows Agent with model selection."""
    print("🤖 Darbot Windows Agent - Enhanced with GitHub Copilot Integration")
    print("=" * 60)
    
    # Check dependencies
    if not check_dependencies():
        sys.exit(1)
    
    # Check environment
    if DOTENV_AVAILABLE:
        load_dotenv()
    
    try:
        from darbot_windows_agent.agent import Agent
        from darbot_windows_agent.github.models import ModelSelector
        
        print("✅ Dependencies loaded successfully")
        
        # Show model selection menu
        model_id, model_selector = display_model_selector_menu()
        
        # Initialize LLM based on selection
        llm = setup_llm_from_selection(model_id, model_selector)
        
        if not llm:
            print("\n💡 To use the agent, you can:")
            print("   - Set up GitHub authentication for Copilot models")
            print("   - Set GOOGLE_API_KEY in environment or .env file")
            print("   - Set OPENAI_API_KEY for OpenAI models")
            print("   - Set GROQ_API_KEY for Groq models")
            print("   - Install Ollama for local models")
            sys.exit(1)
        
        # Initialize Agent with model selector
        try:
            agent = Agent(
                llm=llm, 
                browser='chrome', 
                use_vision=False,
                model_selector=model_selector
            )
            print("✅ Agent initialized successfully")
        except Exception as e:
            print(f"❌ Failed to initialize Agent: {e}")
            sys.exit(1)
        
        # Interactive loop
        print("\n🎯 Agent ready! Enter your queries (type 'quit', 'models', or 'github' for special commands)")
        print("\nExamples:")
        print("  - 'Open notepad'")
        print("  - 'What applications are running?'")
        print("  - 'gh repo list' (GitHub CLI commands)")
        print("  - 'gh auth status' (Check GitHub authentication)")
        print("\nSpecial commands:")
        print("  - 'models' - Show model selection menu")
        print("  - 'github' - Quick GitHub authentication")
        print("  - 'quit' - Exit the application")
        print()
        
        while True:
            try:
                query = input("Enter your query: ").strip()
                
                if query.lower() in ['quit', 'exit', 'q']:
                    print("👋 Goodbye!")
                    break
                
                if query.lower() == 'models':
                    # Re-show model selection
                    new_model_id, _ = display_model_selector_menu()
                    if new_model_id and new_model_id != model_id:
                        new_llm = setup_llm_from_selection(new_model_id, model_selector)
                        if new_llm:
                            agent.llm = new_llm
                            model_id = new_model_id
                            print(f"✅ Switched to new model: {new_model_id}")
                    continue
                
                if query.lower() == 'github':
                    # Quick GitHub setup
                    from darbot_windows_agent.github.auth import GitHubAuth
                    github_auth = GitHubAuth()
                    result, success = github_auth.login()
                    print(result)
                    continue
                
                if not query:
                    continue
                
                print(f"🔄 Processing: {query}")
                try:
                    agent.print_response(query)
                except Exception as e:
                    print(f"❌ Error processing query: {e}")
                    print("💡 Try a different query or check system permissions")
                
                print()  # Add spacing between queries
                
            except KeyboardInterrupt:
                print("\n👋 Goodbye!")
                break
            except EOFError:
                print("\n👋 Goodbye!")
                break
    
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        print("💡 Please check the installation and try again")
        sys.exit(1)

if __name__ == "__main__":
    main()