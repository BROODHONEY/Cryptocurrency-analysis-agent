from langchain_groq import ChatGroq
from typing import List, Dict, Any

class ReportWriter:
    """Generates comprehensive analysis reports using LLM"""

    def __init__(self, llm: ChatGroq):
        self.llm = llm

    def generate_report(self, 
                        crypto: str, 
                        news_data: List[Dict],
                        price_data: Dict) -> str:
        """Generates a comprehensive anaysis report."""

        news_summary = self._format_news(news_data)
        price_summary = self._format_price_data(price_data)

        prompt = f"""You are a professional cryptocurrency analyst. 
                    Generate a comprehensive market analysis report.

                    Cryptocurrency: {crypto}

                    PRICE DATA:
                    {price_summary}

                    RECENT NEWS:
                    {news_summary}

                    Generate a professional report with these sections:
                    1. Executive Summary (2-3 sentences overview)
                    2. Price Analysis (discuss trends, volatility, key levels)
                    3. Market Sentiment (based on news, what's the mood?)
                    4. Risk Assessment (what are the risks?)
                    5. Outlook & Recommendations (what should investors watch?)

                    Keep it professional, data-driven, and actionable. Use the actual numbers provided.

                    Report:
                """
        
        response = self.llm.invoke(prompt)

        return response.content

    def _format_news(self, news_data: List[Dict]) -> str:
        """Format news data for the LLM."""

        if not news_data:
            return "No recent news articles available."
        
        formatted = []
        for i, article in enumerate(news_data, 1):

            title = article.get("title", "No Title")
            url = article.get("url", "No URL")
            highlights = article.get("highlights", "No Highlights")[:150]

            formatted.append(f"Article {i}:\nTitle: {title}\nURL: {url}\nHighlights: {highlights}\n")
            pass

        return "\n\n".join(formatted)
    
    def _format_price_data(self, price_data: Dict) -> str:
        """Format price data for the LLM."""

        if "error" in price_data:
            return "Price data is unavailable."

        return f"""Current Price: ${price_data.get('current_price', 0):,.2f}
                    Starting Price (7d ago): ${price_data.get('start_price', 0):,.2f}
                    Price Change: ${price_data.get('price_change', 0):,.2f} ({price_data.get('price_change_percent', 0):+.2f}%)
                    Highest: ${price_data.get('highest_price', 0):,.2f}
                    Lowest: ${price_data.get('lowest_price', 0):,.2f}
                    Volatility: {price_data.get('volatility', 0):.2f}%
                    Days Analyzed: {price_data.get('days_analyzed', 0)}
                """

if __name__ == "__main__":
    import os
    from dotenv import load_dotenv
    from price_analyzer import PriceAnalyzer
    from news_analyzer import NewsAnalyzer
    
    load_dotenv()
    
    llm = ChatGroq(
        api_key=os.getenv("GROQ_API_KEY"),
        model="llama-3.3-70b-versatile",
        temperature=0.3,
        max_tokens=1500,
        timeout=60,
        max_retries=2,
    )
    
    price_analyzer = PriceAnalyzer()
    news_analyzer = NewsAnalyzer()
    report_writer = ReportWriter(llm)
    
    # Get data
    crypto = "Bitcoin"
    print(f"📊 Gathering data for {crypto}...\n")
    
    price_data = price_analyzer.fetch_price_data(crypto, days=7)
    news_data = news_analyzer.fetch_news(crypto, num_results=10)
    
    # Generate report
    print("✍️  Generating report...\n")
    print("=" * 70)
    
    report = report_writer.generate_report(crypto, news_data, price_data)
    
    print(report)
    print("=" * 70)
