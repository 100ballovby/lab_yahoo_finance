import os
import json
import requests
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib import rcParams
from datetime import datetime

KEY = os.environ.get('API_KEY')
HOST = os.environ.get('API_HOST')

symbol_string = ''
data = {}


def fetchStockData(symbol: str, region: str, api_key: str, api_host: str) -> dict or None:
    """
    Function connects to the API and fetch data through the query string,
    and receives data for building a chart
    :param symbol: Company index on the stock exchange (AAPL, YH, TSLA)
    :param region: Stock region US|BR|AU|DE|ES|GB
    :param api_key: Private api key (yours)
    :param api_host: API host name from rapidapi.com
    :return: body of the response in JSON format
    """
    url = 'https://apidojo-yahoo-finance-v1.p.rapidapi.com/market/get-charts'
    querystring = {
        'symbol': symbol.upper(),
        'interval': '5m',
        'range': '5d',
        'region': region.upper()
    }
    headers = {
        'x-rapidapi-host': api_host,
        'x-rapidapi-key': api_key
    }
    response = requests.get(url, headers=headers, params=querystring)
    json_r = json.loads(response.text)

    if response.status_code == 200:
        return json_r
    else:
        return None


def parseTimestamp(data: dict) -> list:
    """
    API returns a lot of daata for a stock symbol. All of it's formatted
    as a separate series of opening and closing, high and low figures of the stock
    during each day.
    :param data: json response
    :return: list of dates
    """
    timestamp_list = []
    timestamp_list.extend(data['chart']['result'][0]['timestamp'])
    timestamp_list.extend(data['chart']['result'][0]['timestamp'])
    calendar_time = []
    for ts in timestamp_list:
        dt = datetime.fromtimestamp(ts)
        calendar_time.append(dt.strftime('%d/%m/%Y'))
    return calendar_time

with open('yahoo.json', 'r') as j:
    o = j.read()
    o = json.loads(o)
    print(parseTimestamp(o))

#fetch = fetchStockData('TSLA', 'US', KEY, HOST)
#with open('yahoo.json', 'w') as f:
#    f.write(json.dumps(fetch, indent=4))


