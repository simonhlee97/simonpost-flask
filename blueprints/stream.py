import streamlit as st
import pandas as pd
from PIL import Image

st.write("""
# Stock Market Application
**Visually** show stock data. From January 4 2020 to August 4 2020
""")

image = Image.open('/Users/simonlee/Downloads/flask_projects/simon_flask_proj/static/images/wallst.jpg')

st.image(image, use_column_width=True)

st.sidebar.header('User Input')

# function to get user's input
def get_input():
    start_date = st.sidebar.text_input("Start Date", "2020-01-02")
    end_date = st.sidebar.text_input("End Date", "2020-08-04")
    stock_symbol = st.sidebar.text_input("Stock Symbol", "AMZN")
    return start_date, end_date, stock_symbol

# function to get Company Name
def get_company_name(symbol):
    if symbol == "AMZN":
        return 'Amazon'
    elif symbol == "TSLA":
        return 'Tesla'
    elif symbol == 'GOOG':
        return 'Alphabet'
    else:
        'None'


def get_data(symbol, start, end):
    # load data
    if symbol.upper() == 'AMZN':
        df = pd.read_csv('static/data/amazon.csv')
    elif symbol.upper() == 'TSLA':
        df = pd.read_csv('static/data/tesla.csv')
    elif symbol.upper() == 'GOOG':
        df = pd.read_csv('static/data/google.csv')
    else:
        df = pd.DataFrame(columns=['Date', 'Close', 'Open', 'Volume', 'Adj Close', 'High', 'Low'])
    start = pd.to_datetime(start)
    end = pd.to_datetime(end)

    start_row=0
    end_row=0

    for i in range(0, len(df)):
        if start <= pd.to_datetime(df['Date'][i]):
            start_row=i
            break

    for j in range(0, len(df)):
        if end >= pd.to_datetime(df['Date'][len(df)-1-j]):
            end_row=len(df)-1-j
            break
    
    # set index to be the date
    df = df.set_index(pd.DatetimeIndex(df['Date'].values))

    return df.iloc[start_row:end_row + 1, :]

# get user input
start, end, symbol = get_input()
#get data
df = get_data(symbol, start, end)
# get company name
company_name=get_company_name(symbol.upper())

#display closing price
st.header(company_name+" Close Price\n")
st.line_chart(df['Close'])

#display the volume
st.header(company_name+" Volume\n")
st.line_chart(df['Volume'])

st.header('Data Stats')
st.write(df.describe())
