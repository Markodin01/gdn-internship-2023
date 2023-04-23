Currency Exchange App
=====================

This is a API application that provides information about currency exchange rates. It makes use of the [NBP API](http://api.nbp.pl/) to retrieve exchange rate data.

Installation
------------

1.  Clone this repository to your local machine.
2.  Install the required dependencies by running `pip install -r requirements.txt`.
3.  Run it with `flask --app=api/services/app.py run -h localhost -p 8080`.

Usage
-----

The application consists of a single file, `app.py`, which provides three functions for retrieving exchange rate data:

### `get_average_exchange_rate(currency: str, date: str) -> float`

Given a date (formatted `YYYY-MM-DD`) and a currency code, returns the average exchange rate for that currency on the given date.

### `get_max_min_average(currency: str, n: int) -> dict`

Given a currency code and the number of last quotations, returns a dictionary with the max and min average exchange rates for that currency over the last n days.

### `get_major_difference(currency: str, n: int) -> float`

Given a currency code and the number of last quotations, returns the major difference between the buy and sell rates over the last n days.


Examples
--------



Here are some examples of how to use the functions:

```python:
from app import get_average_exchange_rate, get_max_min_average, get_major_difference
```

# Get the average exchange rate for USD on January 1, 2022

```python:
rate = get_average_exchange_rate('USD', '2022-01-01')

print(f'The average exchange rate for USD on January 1, 2022 was {rate}')
```

# Get the max, min, and average exchange rates for EUR over the last 30 days

```python:
rates = get_max_min_average('EUR', 30)

print(f'The max exchange rate for EUR over the last 30 days was {rates["max"]}')

print(f'The min exchange rate for EUR over the last 30 days was {rates["min"]}')

print(f'The average exchange rate for EUR over the last 30 days was {rates["average"]}')
```

# Get the major difference between the buy and sell rates for GBP over the last 7 days

```python:
diff = get_major_difference('GBP', 7)
print(f'The major difference between the buy and sell rates for GBP over the last 7 days was {diff}')
```

License
-------

This project is a part of an internship application process.