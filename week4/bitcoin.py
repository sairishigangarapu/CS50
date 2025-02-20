import sys
import requests
import json
def main():
      coin = price()
      coin_price(coin)
def price():
        if len(sys.argv) == 2 :
                try:
                    if float(sys.argv[1]):
                           return sys.argv[1]
                except ValueError:
                    sys.exit("Command-line argument is not a number")
        else:
              sys.exit("Missing command-line argument")

def coin_price(coin):
      x = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
      y = x.json()
      z = ((float(sys.argv[1]))*(float(y["bpi"]["USD"]["rate_float"])))
      print(f"${z:,.4f}")

main()

