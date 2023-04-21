import requests
from datetime import datetime, timedelta

NBP_BASE_URL = 'http://api.nbp.pl/api/exchangerates'

def get_average_exchange_rate(date: str, currency: str) -> float:
    """
    Given a date (formatted YYYY-MM-DD) and a currency code, returns the
    average exchange rate for that currency on the given date.
    """
    url = f'{NBP_BASE_URL}/rates/A/{currency}/{date}/'
    response = requests.get(url)
    data = response.json()
    rates = data.get('rates', [])
    if len(rates) > 0:
        return rates[0].get('mid', 0)
    else:
        return 0

def get_min_max_average(currency: str, n: int) -> dict:
    """
    Given a currency code and the number of last quotations, returns a
    dictionary with the max and min average exchange rates for that currency
    over the last n days.
    """
    today = datetime.today().strftime('%Y-%m-%d')
    url = f'{NBP_BASE_URL}/rates/A/{currency}/last/{n}/'
    response = requests.get(url)
    data = response.json()
    rates = data.get('rates', [])
    if len(rates) == 0:
        return {'max': 0, 'min': 0}
    else:
        total = 0
        min_rate = float('inf')
        max_rate = float('-inf')
        for rate in rates:
            mid = rate.get('mid', 0)
            total += mid
            if mid < min_rate:
                min_rate = mid
            if mid > max_rate:
                max_rate = mid
        avg_rate = total / len(rates)
        return {'max': max_rate, 'min': min_rate, 'average': avg_rate}

def get_buy_sell_difference(currency: str, n: int) -> float:
    """
    Given a currency code and the number of last quotations, returns the
    major difference between the buy and sell rates over the last n days.
    """
    today = datetime.today().strftime('%Y-%m-%d')
    url = f'{NBP_BASE_URL}/rates/C/{currency}/last/{n}/'
    response = requests.get(url)
    data = response.json()
    rates = data.get('rates', [])
    if len(rates) == 0:
        return 0
    else:
        max_diff = float('-inf')
        for rate in rates:
            bid = rate.get('bid', 0)
            ask = rate.get('ask', 0)
            diff = ask - bid
            if diff > max_diff:
                max_diff = diff
        return max_diff
