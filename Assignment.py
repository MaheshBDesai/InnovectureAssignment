import requests
import json

#Code has written in python

#API URL
url = 'https://api.coinlore.net/api/tickers/'

#API response data
response = requests.get('https://api.coinlore.net/api/tickers/', verify=False)
data = response.json()
data = data["data"]

#Filtering BTC and ETH assets
btc_list = list()
eth_list = list()
for symbol in data:
    for k,v in symbol.items():
        if k == "symbol" and v == "BTC":
            ind = data.index(symbol)
            btc_list.append(ind)

        elif k == "symbol" and v == "ETH":
            ind = data.index(symbol)
            eth_list.append(ind)

# Fetching BTC price
for btc in btc_list:
    #BTC asset
    btc_data = data[btc]
    #BTC price
    btc_price = float(btc_data["price_usd"])

#Testing for price falls below $30000
    try:
        assert btc_price > 30000

    except AssertionError:
        print("test case failed because BTC price below $30000")

#Fetching ETH price
for eth in eth_list:
    #ETH asset
    eth_data = data[eth]
    #ETH price
    eth_price = float(eth_data["price_usd"])

#Testing for price falls below $15000
    try:
        assert eth_price > 15000

    except AssertionError:
        print("test case failed because ETH price below $15000")

#Creating and saving a JSON document with all assets whose prices have changed +/- 1% in the last 24 hours
one_percent_price_change_index = list()
le = len(data)
for one_percent_price_change in data:
    for k,v in one_percent_price_change.items():
        # print(k,v)
        if k == "percent_change_24h":
            v = float(v)
            if k == "percent_change_24h" and v >= 1 or v <= (-1):
                one_percent_price_change_index.append(data.index(one_percent_price_change))

one_percent_price_change_data_list = list()
for ind in one_percent_price_change_index:
    one_percent_price_change_data_list.append(data[ind])

#JSON objects written in below mentioned document
json_object  = json.dumps(one_percent_price_change_data_list, indent=4)
with open(r".\assignment.json", "w") as outfile:
    outfile.write(json_object )
