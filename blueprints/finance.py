from flask import Flask, render_template, Blueprint
import requests
finance = Blueprint('finance', __name__)
API_URL = 'https://financialmodelingprep.com/api/v3/stock/real-time-price/{}'
PREP_API_KEY = "f8c29cb31724326cc8cec80b04b3546e"


def fetch_price(ticker):
    data = requests.get('https://financialmodelingprep.com/api/v3/stock/real-time-price/{ticker}'.format(
        ticker.upper()), params={'apikey': API_URL}).json()
    return data["price"]


@finance.route('/stocks/<ticker>')
def stock(ticker):
    price = fetch_price(ticker)
    return render_template('stock_quote.html', ticker=ticker,
                           price=price)


# # # # # # # # #
