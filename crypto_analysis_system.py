import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq

from customer_communicator import CustomerCommunicator, CryptoAnalysisRequest
from price_analyzer import PriceAnalyzer
from news_analyzer import NewsAnalyzer
from report_writer import ReportWriter

load_dotenv()

class CryptoAnalysisSystem:
    """Main orchestrator - brings all agents together"""

    def __init__(self):
        self.llm = ChatGroq(
            api_key=os.getenv("GROQ_API_KEY"),
            model="llama-3.3-70b-versatile",
            temperature=0.3,
            max_tokens=1500,
            timeout=60,
            max_retries=2,
        )

        self.customer_comm = CustomerCommunicator()
        self.price_analyzer = PriceAnalyzer()
        self.news_analyzer = NewsAnalyzer()
        self.report_writer = ReportWriter(self.llm)

        print("✅ Crypto Analysis System initialized!")

    def analyze(self, user_input: str) -> str:
        """Main Analysis workflow - to process user input and generate report"""

        print(f"\n{'='*70}")
        print(f"💬 User Query: '{user_input}'")
        print(f"{'='*70}\n")

        # Step 1: Parse user request
        print("🧠 Parsing your request...")
        request = self.customer_comm.parse_user_request(user_input)

        print(f"   ✓ Cryptocurrency: {request.cryptocurrency}")
        print(f"   ✓ Days: {request.days_history}")
        print(f"   ✓ Include News: {request.include_news}")
        print(f"   ✓ Include Price: {request.include_price_analysis}\n")

        # Step 2: Fetch data
        news_data = []
        price_data = {}

        if request.include_news:
            print("📡 Fetching news data...")
            news_data = self.news_analyzer.fetch_news(request.cryptocurrency, num_results=10)
            print(f"   ✓ Retrieved {len(news_data)} news articles.\n")

        if request.include_price_analysis:
            print("📡 Fetching price data...")
            price_data = self.price_analyzer.fetch_price_data(request.cryptocurrency, days=request.days_history)
            if "error" in price_data:
                print(f"   ⚠️  Price data error: {price_data['error']}\n")
            else:
                print(f"   ✓ Price data retrieved for {price_data.get('days_analyzed', 0)} days.\n")

        # Step 3: Generate report
        print("✍️  Generating report...")
        report = self.report_writer.generate_report(
            request.cryptocurrency,
            news_data,
            price_data
        )
        print("   ✓ Report generation complete!\n")

        return report
    
if __name__ == "__main__":
    print("🚀 CRYPTOCURRENCY ANALYSIS AI SYSTEM")
    print("=" * 70)
    
    # Initialize system
    system = CryptoAnalysisSystem()
    
    # Test with different queries
    test_queries = [
        "What's happening with Bitcoin?",
        "What's the price trend for Dogecoin over the last 30 days?",
        "Analyze Ethereum over the past 14 days",
        "Give me Solana news and price trends"
    ]
    

    query = test_queries[1]  # Try different ones!
    
    report = system.analyze(query)
    
    # Print the final report
    print("\n" + "="*70)
    print("📈 FINAL ANALYSIS REPORT")
    print("="*70)
    print(report)
    print("="*70)