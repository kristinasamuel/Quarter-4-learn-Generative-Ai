from agents import function_tool
import requests 
@function_tool
def get_crypto_price(coin:str = "bitcoins", currencey:str = "usd") -> str:
    url = f"https://api.coinlore.net/api/tickers/"
    response = requests.get(url)
    data = response.json().get("data", {})


    if coin.lower() in data:
        price = data[coin.lower()][currencey.lower()]
        return f"The current price of {coin.capitalize()} in {currencey.upper()} is {price}."
    else:
        return f"Could not retrieve the price for {coin.capitalize()} in {currencey.upper()}. Please check the coin name and currency."


