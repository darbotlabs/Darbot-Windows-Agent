import os
import sys

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
        from langchain_google_genai import ChatGoogleGenerativeAI
    except ImportError:
        missing_deps.append("langchain-google-genai")
    
    try:
        from darbot_windows_agent.agent import Agent
    except ImportError:
        missing_deps.append("darbot-windows-agent (agent module)")
    
    if missing_deps:
        print("❌ Missing required dependencies:")
        for dep in missing_deps:
            print(f"   - {dep}")
        print("\n💡 Please install dependencies:")
        print("   pip install darbot-windows-agent")
        print("   or")
        print("   pip install langchain langchain-google-genai")
        return False
    
    return True

def check_environment():
    """Check if environment is properly configured."""
    if DOTENV_AVAILABLE:
        load_dotenv()
    
    api_key = os.getenv("GOOGLE_API_KEY")
    if not api_key:
        print("⚠️  Warning: GOOGLE_API_KEY not found in environment")
        if not DOTENV_AVAILABLE:
            print("💡 Install python-dotenv to use .env files:")
            print("   pip install python-dotenv")
        print("💡 Set environment variable or create a .env file:")
        print("   GOOGLE_API_KEY=your_api_key_here")
        return False
    
    return True

def main():
    """Main entry point for the Darbot Windows Agent."""
    print("🤖 Darbot Windows Agent - Starting...")
    
    # Check dependencies
    if not check_dependencies():
        sys.exit(1)
    
    # Check environment
    env_ok = check_environment()
    if not env_ok:
        response = input("Continue without API key? (y/N): ")
        if response.lower() != 'y':
            sys.exit(1)
    
    try:
        from langchain_google_genai import ChatGoogleGenerativeAI
        from darbot_windows_agent.agent import Agent
        
        print("✅ Dependencies loaded successfully")
        
        # Initialize LLM
        try:
            llm = ChatGoogleGenerativeAI(model='gemini-2.0-flash')
            print("✅ LLM initialized successfully")
        except Exception as e:
            print(f"❌ Failed to initialize LLM: {e}")
            print("💡 Check your API key and network connection")
            sys.exit(1)
        
        # Initialize Agent
        try:
            agent = Agent(llm=llm, browser='chrome', use_vision=False)
            print("✅ Agent initialized successfully")
        except Exception as e:
            print(f"❌ Failed to initialize Agent: {e}")
            sys.exit(1)
        
        # Interactive loop
        print("\n🎯 Agent ready! Enter your queries (type 'quit' to exit)")
        print("Examples:")
        print("  - 'Open notepad'")
        print("  - 'What applications are running?'")
        print("  - 'Take a screenshot'")
        print()
        
        while True:
            try:
                query = input("Enter your query: ").strip()
                
                if query.lower() in ['quit', 'exit', 'q']:
                    print("👋 Goodbye!")
                    break
                
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