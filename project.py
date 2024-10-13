import sys
import json
import requests

url = "https://api.coinlayer.com/api/live?access_key=fba60dcb81eb8e629bdf35a0a6a8e3c2"
response = requests.get(url)
response= json.loads(response.text)
USD_rate = response["rates"]

url2 = "https://v6.exchangerate-api.com/v6/35f5bfbb9e6edad3df521f26/latest/USD"

response2 = requests.get(url2)
response2 = json.loads(response2.text)
exc_rate = response2["conversion_rates"]



def main():
    print("Convert or View Trending Cryptocurrencies?")
    options = input("Convert or view: ").lower()

    if options == "view":
        print("View top n crptocurrencies")
        n = input("n: ")
        view = top(n)
        for i in view:
            print (i)

    elif options == "convert":
        coin = input("Cryptocurrency symbol(e.g. BTC,ETH): ").upper()
        amount = float(input("amount: "))
        cur = input("enter currency code(e.g. USD,AUD,GBP): ").upper()
        coin_price = float(price(coin))
        total = coin_price * amount
        cur_exc_rate = float(exchange(cur))
        total =  total * cur_exc_rate
        print(f"{amount} {coin} equals {total} {cur}")

    else:
        print("Not a valid option")


def price(s):
    if s in USD_rate:
        return USD_rate[s]
    else:
        sys.exit(f"{s} is not a valid Cryptocurrency")

def exchange(s):
    if s in exc_rate:
        return exc_rate[s]
    else:
        sys.exit(f"{s} is not a valid Currency")

def top(n):
    try:
        n = int(n)
        sorted_rates = sorted(USD_rate.items(), key=lambda x: x[1], reverse=True)[:n]
        print(f"Top {n} most expensive Cryptocurrencies")
        result = []
        for index, (coin, rate) in enumerate(sorted_rates, start=1):
            i = f"{index}. {coin}: {rate} USD"
            result.append(i)
        return result
    except ValueError:
        sys.exit("only accepts integers")

if __name__ == "__main__":
    main()

