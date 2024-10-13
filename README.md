# Crypto Converter
#### Video Demo:  https://youtu.be/wGaLMmgwoPc
#### Description:

This program asks the users if they intend to view the trending cryptocurrencies or convert a specified amount of a cryptocurrency in a any recognized national currency

if they enter "view" it asks them how many cryptocurrencies they would like to view and displays the top n most expensive cryptocurrencies where n is the the number of cryptocurrencies they input to view

if they enter convert it asks for a cryptocurrency symbol, currency code and amount then fetch the current price of that cryptocurrency and outputs the price in the selected national currency

# Libraries
```python
import sys
import json
import requests
```
I Improted the request library to accesses API's

The json library to correctly display the content of said API's

The sys library to exit the code incase of errors

# API's used
#### 1. url = "https://api.coinlayer.com/api/live?access_key=5ed519d5233010031692e11dd0ae6e97"

```python
response = requests.get(url)
response= json.loads(response.text)
USD_rate = response["rates"]
```
>This API was obtained from coinlayer.com and it consists of Cryptocurrency rate in USD

>it is accessed using my own special access key

>This code accesses the url, fetches the cryptocurrency exchange rates in USD and stores them in a dictionary called 'USD_rates'

#### 2. url2 = "https://v6.exchangerate-api.com/v6/35f5bfbb9e6edad3df521f26/latest/USD"

```
response2 = requests.get(url2)
response2 = json.loads(response2.text)
exc_rate = response2["conversion_rates"]
```
>This API was obtained from exchangerate-api.com and it consists of USD exchangerate for other nationally recognized currencies.

>it is also accessed using my own special access key.

>This code accesses the url, fetches the currency exchange rates in USD and stores them in a dictionary called 'exc_rate'

These sections of the code essential fetch the cryptocurrency rate and national currency rate both in USD, it is important that they are both in USD to avoid any inconsistencies in the calculation

# Functions
### Price
```python
def price(s):
    if s in USD_rate:
        return USD_rate[s]
    else:
        sys.exit(f"{s} is not a valid Cryptocurrency")
```
it receives the three-digit Cryptocurrency symbol as a key and returns the exchange rate in USD as output.

it exits the code with an error message if the selected cryptocurrency does not exist.


### Exchange
```python
def exchange(s):
    if s in exc_rate:
        return exc_rate[s]
    else:
        sys.exit(f"{s} is not a valid Currency")
```
it receives the three-digit currency code of a recognized local currency as a key and returns the exchange rate in USD as output

it exits the code with an error message if the selected National currency does not exist.

### Top n
```python
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
```
it receives an integer as input, creates and returns a list of the most expensive cryptocurrencies in descending order, the number of values on the list is based on the integer input.

it exits the code with an error message if the value entered is not an integer.


# About the Coder
Olaoluwa Olowokudejo is a Computer Science student in Lagos, Nigeria. This code was writen for his final project in the CS50 Python course
