import os
import requests
from typing import List, Dict, Any
from dotenv import load_dotenv
from datetime import datetime, timedelta

load_dotenv()

class NewsAnalyzer:
    """Fetches and analyzes cryptocurrency news articles."""

    def __init__(self, exa_api_key: str = None):
        self.exa_api_key = os.getenv("EXA_API_KEY")
        self.base_url = "https://api.exa.ai/search"

    def fetch_news(self, cryptocurrency: str, num_results: int = 10) -> List[Dict[str, Any]]:
        """Fetch recent news articles about a given cryptocurrency."""

        headers = {
            "Authorization": f"Bearer {self.exa_api_key}",
            "Content-Type": "application/json"
        }

        payload = {
            "query": f"{cryptocurrency} cryptocurrency latest news",
            "num_results": num_results,
            "use_autoprompt": True,
            "type": "auto",
            "contents": {
                "text": True,
                "highlights": {
                "max_characters": 200
                }
            }
        
        }

        response = requests.post(self.base_url, json=payload, headers=headers)

        if response.status_code == 200:
            data = response.json()
            return data.get("results", [])
        else:
            return {"error": f"API returned status code {response.status_code}"}
        
    def analyze_sentiment_individual(self, text: str) -> str:
        """Analyzes sentiment of a single news article text."""
        
        positive_keywords = ["surge", "gain", "growth", "bullish", "rise", "up", "positive", "adoption"]
        negative_keywords = ["crash", "fall", "drop", "bearish", "down", "negative", "decline", "loss"]

        positive_count = 0
        negative_count = 0

        text = text.lower()

        for keyword in positive_keywords:
            if keyword in text:
                positive_count += 1

        for keyword in negative_keywords:
            if keyword in text:
                negative_count += 1

        if positive_count > negative_count:
            return "positive"
        elif negative_count > positive_count:
            return "negative"
        else:
            return "neutral"

    def analyze_sentiment(self, news_articles: List[Dict[str, Any]]) -> Dict[str, Any]:
        """Analyzes sentiment of the fetched news articles."""
        
        positive_keywords = ["surge", "gain", "growth", "bullish", "rise", "up", "positive", "adoption"]
        negative_keywords = ["crash", "fall", "drop", "bearish", "down", "negative", "decline", "loss"]

        positive_count = 0
        negative_count = 0

        for article in news_articles:
            text = article.get("text", "").lower()

            for keyword in positive_keywords:
                if keyword in text:
                    positive_count += 1

            for keyword in negative_keywords:
                if keyword in text:
                    negative_count += 1

            if positive_count > negative_count:
                return "positive"
            elif negative_count > positive_count:
                return "negative"
            else:
                return "neutral"
        
if __name__ == "__main__":
    analyzer = NewsAnalyzer()

    crypto = "bitcoin"
    num_articles = 5

    print(f"Fetching news articles for {crypto}...")
    articles = analyzer.fetch_news(crypto, num_articles)

    print(f"Found {len(articles)} articles:\n")  

    print("=" * 40)

    for i, article in enumerate(articles, 1):

        print(f"Article {i}: {article.get('title')}")
        print(f"URL: {article.get('url')}\n")
        print(f"Highlights: {article.get('highlights', 'No highlights available')}\n")
        sentiment = analyzer.analyze_sentiment_individual(article.get('text', ''))
        print(f"Sentiment: {sentiment}\n")
        print("=" * 40)
        pass

    print(f"Analyzing sentiment of the fetched articles...\n")
    sentiment = analyzer.analyze_sentiment(articles)
    print(f"Overall sentiment: {sentiment}")