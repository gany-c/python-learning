import json
import yfinance as yf
import numpy as np



"""

Curl for file download:

curl -X POST https://www.nyse.com/api/quotes/filter -H "Content-Type: application/json" -d '{"instrumentType":"EQUITY","pageNumber":1,"sortColumn":"NORMALIZED_TICKER","sortOrder":"ASC","maxResultsPerPage":7059,"filterToken":""}' > completeNyse.txt
"""

# Calculate RSI
def calculate_RSI(ticker, periods=14):
    # Download stock data
    stock_data = yf.download(ticker, start='2024-01-01', end='2024-03-01')
    delta = stock_data['Close'].diff().dropna()
    gain = delta.where(delta > 0, 0)
    loss = -delta.where(delta < 0, 0)

    gain_percentage = gain / stock_data['Close'].shift(1) * 100
    loss_percentage = loss / stock_data['Close'].shift(1) * 100

    avg_gain = gain_percentage.mean()
    avg_loss = loss_percentage.mean()

    rs = avg_gain / avg_loss
    rsi = 100 - (100 / (1 + rs))
    print("RSI = ", rsi)
    return rsi

tickers = []

with open('/Users/gchidambara/completeNyse.txt', 'r') as file:
    rows = json.load(file)

for item in rows:
    ticker = item['symbolTicker']
    tickers.append(ticker)

print(tickers)
### Remove line before running
# tickers = ['JD']

# Open the file in write mode ('w')
with open('output-stocks.txt', 'w') as f:

    for ticker in tickers:
        rsi = calculate_RSI(ticker)
        if rsi <= 35:
            f.write(f"{ticker} { rsi} \n")
            f.flush()
