from flask import Blueprint, render_template
import requests

STOCK_NAME = "AMZN"
COMPANY_NAME = "Amazon"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

NEWS_API_KEY = "527fbc92efee4e54aee7682e54a139ef"
STOCK_API_KEY = "6SOZN8PU0YEXKRZH"

# Yesterday's closing prices
stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": STOCK_API_KEY,
}

response = requests.get(STOCK_ENDPOINT, params=stock_params)
data = response.json()["Time Series (Daily)"]
data_list = [value for (key, value) in data.items()]
yesterday_data = data_list[0]
yesterday_closing_price = yesterday_data["4. close"]
print(yesterday_closing_price)


# Get the day before yesterday's closing stock price
day_before_yesterday_data = data_list[1]
day_before_yesterday_closing_price = day_before_yesterday_data["4. close"]
print(day_before_yesterday_closing_price)

# Find the positive difference between 1 and 2. e.g. 40 - 20 = -20, but the positive difference is 20. Hint: https://www.w3schools.com/python/ref_func_abs.asp
difference = float(yesterday_closing_price) - \
    float(day_before_yesterday_closing_price)
up_down = None
if difference > 0:
    up_down = "🔺"
else:
    up_down = "🔻"

# Work out the percentage difference in price between closing price yesterday and closing price the day before yesterday.
diff_percent = round((difference / float(yesterday_closing_price)) * 100)
print(diff_percent)


# -----blueprints/simple_templates.py-----
# -----blueprints/simple_templates.py-----
# -----blueprints/simple_templates.py-----


stocks = Blueprint('stocks', __name__)


@stocks.route("/udemy")
def faq():
    yesterday_closing_price = yesterday_data["4. close"]

    if abs(diff_percent) > 1:
        news_params = {
            "apiKey": NEWS_API_KEY,
            "qInTitle": COMPANY_NAME,
        }

        news_response = requests.get(NEWS_ENDPOINT, params=news_params)
        articles = news_response.json()["articles"]
        print(articles)
        three_articles = articles[:4]
        return render_template('udemy.html', three_articles=three_articles, yesterday_closing_price=yesterday_closing_price)
