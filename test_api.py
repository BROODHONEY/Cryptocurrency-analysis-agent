import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
import requests

load_dotenv()

groq_key = os.getenv("GROQ_API_KEY")

llm = ChatGroq(api_key=groq_key, model="meta-llama/llama-4-scout-17b-16e-instruct")

print("Sending request to Groq API...")

response = llm.invoke("What is Bitcoin in one sentence?")

print(f"Question: What is Bitcoin in one sentence?")
print(f"Response from Groq API: {response.content}")

print("Testing CoinGecko API...")
coingecko_response = requests.get(
    "https://api.coingecko.com/api/v3/simple/price",
    params={"ids": "bitcoin", "vs_currencies": "usd"},
)

print(f"CoinGecko API Response Status Code: {coingecko_response.status_code}")

print(f"Bitcoin Price: {coingecko_response.json()['bitcoin']['usd']}")
