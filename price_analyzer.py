import requests
from datetime import datetime
from typing import Dict, Any

class PriceAnalyzer:
    """Fetches and analyzes cryptocurrency price data."""

    def __init__(self):
        self.base_url = "https://api.coingecko.com/api/v3"

        self.coin_map={
            "bitcoin": "bitcoin",
            "btc": "bitcoin",
            "ethereum": "ethereum",
            "eth": "ethereum",
            "ripple": "ripple",
            "litecoin": "litecoin"
        }
    
    def get_coin_id(self, cryptocurrency: str) -> str:
        """converts user input to CoinGecko IDs."""
        if cryptocurrency.lower() in self.coin_map:
            return self.coin_map[cryptocurrency.lower()]
        return cryptocurrency.lower()
    
    def process_price_data(self, data: Dict, cryptocurrency: str) -> Dict[str, Any]:
        """Process raw API data into useful metrics"""

        prices = data.get("prices", [])

        if not prices:
            return {"error": "No price data available"}
        
        price_values = [p[1] for p in prices]

        current_price = price_values[-1]
        start_price = price_values[0]
        highest_price = max(price_values)
        lowest_price = min(price_values)

        change = current_price - start_price
        change_percent = ((current_price - start_price) / start_price) * 100

        volatility = (highest_price - lowest_price) / start_price * 100

        return {
            "cryptocurrency": cryptocurrency,
            "current_price": round(current_price, 2),
            "start_price": round(start_price, 2),
            "highest_price": round(highest_price, 2),
            "lowest_price": round(lowest_price, 2),
            "price_change": round(change, 2),
            "price_change_percent": round(change_percent, 2),
            "volatility": round(volatility, 2),
            "days_analyzed": len(prices)
        }
    
    def fetch_price_data(self, cryptocurrency: str, days: int = 7) -> Dict[str, Any]:
        """Fetches historical price data for a given cryptocurrency."""
        coin_id = self.get_coin_id(cryptocurrency)
        url = f"{self.base_url}/coins/{coin_id}/market_chart"
        params = {
            "vs_currency": "usd",
            "days": days,
            "interval": "daily"
        }
        response = requests.get(url, params=params)
        if response.status_code == 200:
            return self.process_price_data(response.json(), cryptocurrency)
        else:
            return {"error": f"API returned status code {response.status_code}"}
    
if __name__ == "__main__":
    analyzer = PriceAnalyzer()

    crypto = "eth"
    days = 30

    print(f"Fetching price data for {crypto} over the last {days} days...")
    results = analyzer.fetch_price_data(crypto, days)
    
    if "error" in results:
        print(f"Error: {results['error']}")
    else:
        
        print("Price Analysis:")
        for key, value in results.items():
            print(f"{key}: {value}")