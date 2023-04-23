import requests
from datetime import datetime, timedelta
import json

NBP_BASE_URL = 'http://api.nbp.pl/api/exchangerates'

def get_average_exchange_rate(currency: str, date: str) -> float:
    """
    Given a date (formatted YYYY-MM-DD) and a currency code, returns the
    average exchange rate for that currency on the given date.
    """
    url = f'{NBP_BASE_URL}/rates/A/{currency}/{date}/'
    # Construct the API URL to fetch the exchange rate for a given currency on a given date
    response = requests.get(url)
    # Send a GET request to the API and get the response
    content = response.content.decode('utf-8-sig')
    # Decode the response content
    data = json.loads(content)
    # Parse the response content as JSON data
    rates = data.get('rates', [])
    # Get the rates data from the response, or an empty list if there is no data
    if len(rates) > 0:
        return rates[0].get('mid', 0)
    else:
        return 0
    # Return the average exchange rate, or 0 if there is no data

def get_max_min_average(currency: str, n: int) -> dict:
    """
    Given a currency code and the number of last quotations, returns a
    dictionary with the max and min average exchange rates for that currency
    over the last n days.
    """
    today = datetime.today().strftime('%Y-%m-%d')
    # Get the current date in the format YYYY-MM-DD
    url = f'{NBP_BASE_URL}/rates/A/{currency}/last/{n}/'
    # Construct the API URL to fetch the last n days of exchange rate data for a given currency
    response = requests.get(url)
    # Send a GET request to the API and get the response
    data = response.json()
    # Parse the response content as JSON data
    rates = data.get('rates', [])
    # Get the rates data from the response, or an empty list if there is no data
    if len(rates) == 0:
        return {'max': 0, 'min': 0}
    else:
        total = 0
        min_rate = float('inf')
        max_rate = float('-inf')
        # Initialize the total exchange rate, minimum exchange rate, and maximum exchange rate
        for rate in rates:
            mid = rate.get('mid', 0)
            total += mid
            # Add the mid exchange rate to the total
            if mid < min_rate:
                min_rate = mid
            # Update the minimum exchange rate if the current mid exchange rate is lower
            if mid > max_rate:
                max_rate = mid
            # Update the maximum exchange rate if the current mid exchange rate is higher
        avg_rate = total / len(rates)
        # Calculate the average exchange rate over the last n days
        return {'max': max_rate, 'min': min_rate, 'average': avg_rate}
    # Return a dictionary containing the max, min, and average exchange rates

def get_major_difference(currency: str, n: int) -> float:
    """
    Given a currency code and the number of last quotations, returns the
    major difference between the buy and sell rates over the last n days.
    """
    # Get the current date
    today = datetime.today().strftime('%Y-%m-%d')
    # Build the URL for the API call
    url = f'{NBP_BASE_URL}/rates/C/{currency}/last/{n}/'
    # Send the request to the API and get the response
    response = requests.get(url)
    # Extract the JSON data from the response
    data = response.json()
    # Get the list of rates from the JSON data
    rates = data.get('rates', [])
    if len(rates) == 0:
        # If there are no rates, return 0
        return 0
    else:
        # Otherwise, initialize the max_diff variable to negative infinity
        max_diff = float('-inf')
        # Iterate over each rate in the list
        for rate in rates:
            # Get the bid and ask prices from the rate
            bid = rate.get('bid', 0)
            ask = rate.get('ask', 0)
            # Calculate the difference between the ask and bid prices
            diff = ask - bid
            # If the difference is greater than the current max_diff, update max_diff
            if diff > max_diff:
                max_diff = diff
        # Return the maximum difference between the buy and sell prices
        return max_diff

