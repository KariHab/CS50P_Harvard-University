import sys
import requests


n_bitcoin = sys.argv[1]

if sys.argv[1]== "0":
    print("cannot be zero")

if sys.argv[1].isalpha():
    print("have to be a number")


response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
o = response.json()
rate = o["bpi"]["USD"]["rate_float"]
price = float(n_bitcoin) * rate
print(f"${price:,.4f}")