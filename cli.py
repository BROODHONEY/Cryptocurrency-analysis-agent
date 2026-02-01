import os
import sys
from datetime import datetime
from crypto_analysis_system import CryptoAnalysisSystem


class CryptoCLI:
    """Interactive command-line interface for crypto analysis"""
    
    def __init__(self):
        self.system = None
        self.reports_folder = "reports"
        
        # Ensure reports folder exists
        os.makedirs(self.reports_folder, exist_ok=True)
    
    def print_banner(self):
        """Display welcome banner"""
        banner = """
╔══════════════════════════════════════════════════════════════╗
║                                                              ║
║     🚀 CRYPTOCURRENCY ANALYSIS AI SYSTEM 🚀                 ║
║                                                              ║
║     Powered by LangChain + Groq + Llama 3                   ║
║                                                              ║
╚══════════════════════════════════════════════════════════════╝
        """
        print(banner)
    
    def initialize_system(self):
        """Initialize the AI system"""
        print("🔄 Initializing AI agents...")
        
        try:
            self.system = CryptoAnalysisSystem()
            print("✅ System ready!\n")
            return True
        except Exception as e:
            print(f"❌ Failed to initialize: {e}")
            return False
    
    def save_report(self, report: str, cryptocurrency: str) -> str:
        """Save report to a file"""
        
        timestamp = datetime.now().strftime("%Y-%m-%d_%H%M%S")
        filename = f"{cryptocurrency}_{timestamp}.md"
        
        filepath = os.path.join(self.reports_folder, filename)
        
        try:
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(report)
            
            return filepath
        except Exception as e:
            print(f"❌ Error saving report: {e}")
            return None
    
    def run_analysis(self, query: str):
        """Run analysis and handle the report"""
        
        try:
            report = self.system.analyze(query)
            
            # Display the report
            print("\n" + "="*70)
            print("📈 ANALYSIS REPORT")
            print("="*70)
            print(report)
            print("="*70 + "\n")
            
            # Ask if user wants to save
            save = input("💾 Save this report? (y/n): ").strip().lower()
            
            if save in ['y', 'yes']:
                # TODO: Extract cryptocurrency name from query for filename
                # Simple approach: just use first word or ask user
                crypto = input("   Enter crypto name for filename (e.g., Bitcoin): ").strip()
                
                # TODO: Save the report
                filepath = self.save_report(report, crypto)
                
                if filepath:
                    print(f"✅ Report saved to: {filepath}")
            
            return True
            
        except Exception as e:
            print(f"❌ Error during analysis: {e}")
            return False
    
    def run(self):
        """Main interactive loop"""
        
        self.print_banner()
        
        # Initialize system
        if not self.initialize_system():
            print("Cannot start without successful initialization.")
            return
        
        print("💡 Tips:")
        print("   - Ask naturally: 'What's happening with Bitcoin?'")
        print("   - Be specific: 'Analyze Ethereum over 14 days'")
        print("   - Type 'quit' or 'exit' to stop\n")
        print("="*70)
        
        # Main interaction loop
        while True:
            print()
            # TODO: Get user input
            query = input("🔍 Your question: ").strip()
            
            # Check if user wants to quit
            if query.lower() in ['quit', 'exit', 'q', 'bye']:
                print("\n👋 Thanks for using Crypto Analysis AI!")
                print("   Stay informed, invest wisely! 🚀\n")
                break
            
            # Skip empty inputs
            if not query:
                print("⚠️  Please enter a question.")
                continue
            
            # Run analysis
            self.run_analysis(query)
            
            # Ask if they want to continue
            print()
            continue_prompt = input("❓ Ask another question? (y/n): ").strip().lower()
            
            if continue_prompt not in ['y', 'yes', '']:
                print("\n👋 Thanks for using Crypto Analysis AI!")
                print("   Stay informed, invest wisely! 🚀\n")
                break


if __name__ == "__main__":
    cli = CryptoCLI()
    
    try:
        cli.run()
    except KeyboardInterrupt:
        print("\n\n⚠️  Interrupted by user")
        print("👋 Goodbye!\n")
        sys.exit(0)