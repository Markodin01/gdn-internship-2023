from flask import Flask, jsonify, request
from nbp_handler import get_exchange_rate, get_max_min_average, get_major_difference
#from instance.config import Config

app = Flask(__name__)
#app.config.from_object(Config)

@app.route('/exchanges/<currency>/<date>')
def get_exchange_rate_route(currency, date):
    rate = get_exchange_rate(currency, date)
    if rate is None:
        return jsonify(error='Data not available'), 404
    return jsonify(rate=rate)

@app.route('/exchanges/<currency>/max-min/<int:n>')
def get_max_min_average_route(currency, n):
    result = get_max_min_average(currency, n)
    if result is None:
        return jsonify(error='Data not available'), 404
    return jsonify(result)

@app.route('/exchanges/<currency>/major-difference/<int:n>')
def get_major_difference_route(currency, n):
    result = get_major_difference(currency, n)
    if result is None:
        return jsonify(error='Data not available'), 404
    return jsonify(result)

if __name__ == '__main__':
    app.run()
