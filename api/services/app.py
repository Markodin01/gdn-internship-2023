from flask import Flask, jsonify, request
from nbp_handler import get_average_exchange_rate, get_max_min_average, get_major_difference
from flask_cors import CORS
from config import Config

# Create a new Flask app instance
app = Flask(__name__)

# Enable Cross-Origin Resource Sharing (CORS) for the app
CORS(app)

# Load configuration from config.py file
app.config.from_object(Config)

# Define a route for getting the average exchange rate for a currency and date
@app.route('/exchanges/<currency>/<date>')
def get_average_exchange_rate_route(currency, date) -> float:
    # Call the get_average_exchange_rate function from nbp_handler to get the rate
    rate = get_average_exchange_rate(currency, date)
    # If the rate is None (i.e. data is not available), return a 404 error message
    if rate is None:
        return jsonify(error='Data not available'), 404
    # Otherwise, return the rate in a JSON format
    return jsonify(rate=rate)

# Define a route for getting the max, min, and average exchange rates for a currency over a specified number of days
@app.route('/exchanges/<currency>/max-min/<int:n>')
def get_max_min_average_route(currency, n) -> dict:
    # Call the get_max_min_average function from nbp_handler to get the result
    result = get_max_min_average(currency, n)
    # If the result is None (i.e. data is not available), return a 404 error message
    if result is None:
        return jsonify(error='Data not available'), 404
    # Otherwise, return the result in a JSON format
    return jsonify(result)

# Define a route for getting the major differences in exchange rates for a currency over a specified number of days
@app.route('/exchanges/<currency>/major-difference/<int:n>')
def get_major_difference_route(currency, n) -> float:
    # Call the get_major_difference function from nbp_handler to get the result
    result = get_major_difference(currency, n)
    # If the result is None (i.e. data is not available), return a 404 error message
    if result is None:
        return jsonify(error='Data not available'), 404
    # Otherwise, return the result in a JSON format
    return jsonify(result)

# Start the app if this script is being run directly (i.e. not imported as a module)
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
