import os 
import json
from dataclasses import dataclass
from langchain_groq import ChatGroq
from dotenv import load_dotenv

load_dotenv()

@dataclass
class CryptoAnalysisRequest:
    """Structure for what the user wants"""
    cryptocurrency: str
    days_history: int
    include_news: bool = True
    include_price_analysis: bool = True

class CustomerCommunicator:
    """Parses user input using LLM"""

    def __init__(self, groq_api_key: str = None):
        self.groq_api_key = groq_api_key or os.getenv("GROQ_API_KEY")
        self.llm = ChatGroq(api_key=self.groq_api_key, model="llama-3.3-70b-versatile")

    def parse_user_request(self, user_input: str) -> CryptoAnalysisRequest:
        """Convert natural language to structured request"""

        prompt = f"""You are a cryptocurrency analysis assistant. 
                Extract the following information from the user's request:

                User request: "{user_input}"

                Extract:
                1. Which cryptocurrency they're asking about (Bitcoin, Ethereum, etc.)
                2. How many days of history they want (default: 7)
                3. Do they want news analysis? (default: yes)
                4. Do they want price analysis? (default: yes)

                Respond ONLY with valid JSON in this EXACT format (no extra text):
                {{"cryptocurrency": "Bitcoin", "days_history": 7, "include_news": true, "include_price_analysis": true}}
                
                JSON:"""
        
        try:
            response = self.llm.invoke(prompt)
            json_text = response.content
            json_text = json_text.strip()
            data = json.loads(json_text)
            return CryptoAnalysisRequest(**data)
        
        except Exception as e:
            print(f"LLM parsing failed: {e}")
            print("    Using fallback keyword matching...")
            return self._fallback_parse(user_input)
        
    def _fallback_parse(self, user_input: str) -> CryptoAnalysisRequest:
        """Simple keyword-based fallback parsing."""
        
        user_input_lower = user_input.lower()

        # Default values
        if "ethereum" in user_input_lower or "eth" in user_input_lower:
            crypto = "Ethereum"
        elif "cardano" in user_input_lower or "ada" in user_input_lower:
            crypto = "Cardano"
        elif "solana" in user_input_lower or "sol" in user_input_lower:
            crypto = "Solana"
        elif "litecoin" in user_input_lower or "ltc" in user_input_lower:
            crypto = "Litecoin"
        else:
            crypto = "Bitcoin"
        
        days_history = 7
        if "14 days" in user_input_lower or "two weeks" in user_input_lower:
            days_history = 14
        elif "30 days" in user_input_lower or "month" in user_input_lower:
            days = 30
        elif "2 days" in user_input_lower or "48 hours" in user_input_lower or "two days" in user_input_lower:
            days_history = 3
        elif "1 day" in user_input_lower or "24 hours" in user_input_lower or "one day" in user_input_lower:
            days_history = 1
        

        include_news = "news" in user_input_lower or "sentiment" in user_input_lower
        include_price_analysis = "price" in user_input_lower or "trend" in user_input_lower

        if not include_news and not include_price_analysis:
            include_news = True
            include_price_analysis = True

        return CryptoAnalysisRequest(
            cryptocurrency=crypto,
            days_history=days_history,
            include_news=include_news,
            include_price_analysis=include_price_analysis
        )
    
if __name__ == "__main__":
    communicator = CustomerCommunicator()
    
    # Test different user inputs
    test_queries = [
        "What's happening with Bitcoin?",
        "Analyze Ethereum over the past 14 days",
        "Give me Solana news only",
        "Show me Cardano price trends for 30 days",
        "How's BTC doing lately?"
    ]
    
    print("🧪 Testing Customer Communicator\n")
    print("=" * 60)
    
    for query in test_queries:
        print(f"\n📝 User: '{query}'")

        request = communicator.parse_user_request(query)   

        print(f"✅ Extracted:")
        print(f"   Cryptocurrency: {request.cryptocurrency}")
        print(f"   Days: {request.days_history}")
        print(f"   Include News: {request.include_news}")
        print(f"   Include Price: {request.include_price_analysis}")