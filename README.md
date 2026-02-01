# 🚀 Cryptocurrency Analysis AI System

An intelligent multi-agent AI system for automated cryptocurrency market analysis powered by LangChain, Groq (Llama 3), and real-time data sources.

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![LangChain](https://img.shields.io/badge/LangChain-Latest-green.svg)
![Groq](https://img.shields.io/badge/Groq-Llama%203-orange.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

## ✨ Features

- 🤖 **AI-Powered Analysis** - Uses Llama 3 (70B) via Groq for natural language understanding
- 📊 **Real-Time Price Data** - Fetches live cryptocurrency prices from CoinGecko
- 📰 **News Integration** - Gets latest market news via Exa API
- 💬 **Natural Language Interface** - Ask questions in plain English
- 📈 **Comprehensive Reports** - AI-generated professional market analysis
- 💾 **Report Export** - Save analysis reports with timestamps
- 🎯 **Multi-Agent Architecture** - Specialized agents for different tasks

## 🏗️ Architecture

The system uses a multi-agent architecture with specialized components:
```
┌─────────────────────────────────────────────┐
│         Customer Communicator               │
│     (Understands natural language)          │
└──────────────┬──────────────────────────────┘
               │
       ┌───────┴────────┐
       │                │
┌──────▼──────┐  ┌─────▼──────┐
│    News     │  │   Price    │
│  Analyzer   │  │  Analyzer  │
└──────┬──────┘  └─────┬──────┘
       │                │
       └───────┬────────┘
               ▼
     ┌─────────────────┐
     │ Report Writer   │
     │  (AI Synthesis) │
     └─────────────────┘
```

### Components

1. **CustomerCommunicator** - Parses user queries using LLM
2. **PriceAnalyzer** - Fetches historical price data and calculates metrics
3. **NewsAnalyzer** - Retrieves latest cryptocurrency news
4. **ReportWriter** - Synthesizes data into comprehensive reports
5. **CryptoAnalysisSystem** - Orchestrates all agents

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- Groq API key (required) - [Get it here](https://console.groq.com)
- Exa API key (optional) - [Get it here](https://exa.ai)

### Installation

1. **Clone the repository**
```bash
git clone https://github.com/yourusername/crypto-analysis-ai.git
cd crypto-analysis-ai
```

2. **Install dependencies**
```bash
pip install -r requirements.txt
```

3. **Set up environment variables**

Create a `.env` file:
```bash
GROQ_API_KEY=your_groq_api_key_here
EXA_API_KEY=your_exa_api_key_here  # Optional
```

4. **Run the CLI**
```bash
python cli.py
```

## 💻 Usage

### Interactive CLI
```bash
python cli.py
```

The CLI provides an interactive interface:
- Ask questions in natural language
- View real-time analysis
- Save reports to files
- Multiple queries in one session

**Example queries:**
- "What's happening with Bitcoin?"
- "Analyze Ethereum over the past 14 days"
- "Give me Solana news and price trends"
- "Show me Cardano performance for 30 days"


## 📊 Sample Output
```
🔍 Your question: What's happening with Bitcoin?

🤖 Step 1: Understanding your request...
   ✓ Cryptocurrency: Bitcoin
   ✓ Days: 7
   ✓ Include News: True
   ✓ Include Price: True

📰 Step 2a: Fetching latest news...
   ✓ Found 10 articles

💹 Step 2b: Analyzing price trends...
   ✓ Analyzed 7 days of data

✍️  Step 3: Generating comprehensive report...
   ✓ Report complete!

======================================================================
📈 ANALYSIS REPORT
======================================================================

## Executive Summary
Bitcoin is currently trading at $45,234.56, showing a 5.2% upward 
trend over the past 7 days with moderate volatility and positive 
market sentiment driven by institutional adoption news.

## Price Analysis
- Current Price: $45,234.56
- 7-Day Change: +$2,345.67 (+5.2%)
- Volatility: 7.2%
- Key Levels: Support at $43,000, Resistance at $47,000

## Market Sentiment
Based on recent news analysis, sentiment is POSITIVE with major 
developments including institutional investments and network upgrades.

## Risk Assessment
Moderate risk with normal market volatility. Watch for regulatory 
developments and macroeconomic factors.

## Outlook & Recommendations
Bullish short-term outlook. Monitor resistance at $47,000...

======================================================================
```

## 📁 Project Structure
```
crypto-analysis-ai/
├── cli.py                      # Interactive command-line interface
├── crypto_analysis_system.py   # Main orchestrator
├── customer_communicator.py    # Natural language parser
├── price_analyzer.py           # Price data fetcher
├── news_analyzer.py            # News data fetcher
├── report_writer.py            # Report generator
├── requirements.txt            # Python dependencies
├── .env                        # API keys (not in repo)
├── reports/                    # Saved reports folder
└── README.md                   # This file
```

## Technologies Used

- **[LangChain](https://python.langchain.com/)** - Framework for LLM applications
- **[Groq](https://groq.com/)** - Ultra-fast LLM inference
- **[Llama 3.3 70B](https://huggingface.co/meta-llama)** - Meta's large language model
- **[CoinGecko API](https://www.coingecko.com/en/api)** - Cryptocurrency price data
- **[Exa API](https://exa.ai/)** - AI-powered search for news
- **Python 3.8+** - Programming language

## What I Learned

Building this project taught me:

- Multi-agent system architecture
- LangChain framework and agent orchestration
- Working with LLMs (Llama 3 via Groq)
- Prompt engineering for structured outputs
- API integration and error handling
- Natural language processing
- Data aggregation and synthesis
- Building production-ready Python applications

## 🔮 Future Enhancements

- [ ] Add technical indicators (RSI, MACD, Bollinger Bands)
- [ ] Implement price prediction using ML
- [ ] Add portfolio tracking
- [ ] Real-time price alerts
- [ ] Web dashboard with Flask/FastAPI
- [ ] Multi-cryptocurrency comparison
- [ ] Historical data storage with database
- [ ] Social media sentiment analysis (Twitter, Reddit)
- [ ] Telegram/Discord bot integration
- [ ] Email report delivery

## 🔑 API Keys

### Groq (Required)
1. Visit [console.groq.com](https://console.groq.com)
2. Sign up for free
3. Create API key
4. Add to `.env` file

### Exa (Optional)
1. Visit [exa.ai](https://exa.ai)
2. Sign up
3. Get API key
4. Add to `.env` file

*Note: The system works without Exa API key using fallback mock data*

## 📄 License

MIT License - feel free to use this project for learning and development!

## 🙏 Acknowledgments

- **Anthropic** for Claude AI assistance in development
- **Meta** for Llama 3
- **Groq** for ultra-fast inference
- **CoinGecko** for free crypto data API
- **Exa** for AI-powered search

## 📧 Contact

Questions? Suggestions? Feel free to open an issue!

---

**Built with ❤️ using LangChain, Groq, and Llama 3**

⭐ Star this repo if you found it helpful!