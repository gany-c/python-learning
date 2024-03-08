import json
import yfinance as yf
import numpy as np

"""
Curl for file download:

curl -X POST https://www.nyse.com/api/quotes/filter -H "Content-Type: application/json" -d '{"instrumentType":"EQUITY","pageNumber":1,"sortColumn":"NORMALIZED_TICKER","sortOrder":"ASC","maxResultsPerPage":7059,"filterToken":""}'


"""

# Calculate RSI
def calculate_RSI(ticker, periods=14):
    # Download stock data
    stock_data = yf.download(ticker, start='2024-01-01', end='2024-03-01')
    delta = stock_data['Close'].diff().dropna()
    gain = delta.where(delta > 0, 0)
    loss = -delta.where(delta < 0, 0)

    avg_gain = gain.rolling(window=periods).mean()
    avg_loss = loss.rolling(window=periods).mean()

    rs = avg_gain / avg_loss
    rsi = 100 - (100 / (1 + rs))
    print("RSI = ", rsi)
    print(rsi.shape)    
    return rsi[-1] if len(rsi) > 0 else np.nan

tickers = []

with open('/Users/gchidambara/Desktop/completeNyse.txt', 'r') as file:
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
