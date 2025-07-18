# yahoo_scrapper.py

import yfinance as yf
import pandas as pd
from datetime import datetime

# List of B3 tickers with .SA suffix
tickers = ['BBAS3.SA', 'BBSE3.SA', 'BRBI11.SA', 'CMIN3.SA', 'ISAE4.SA', 'KLBN11.SA']

# Download today's data (or last available)
data = yf.download(tickers=tickers, period="1d", interval="1d", group_by="ticker", auto_adjust=True)

# Extract closing prices
rows = []
for ticker in tickers:
    try:
        close = data[ticker]['Close'].iloc[-1]
        date = data[ticker]['Close'].index[-1].strftime('%Y-%m-%d')
        rows.append({'Ticker': ticker, 'Price': close, 'Date': date})
    except Exception as e:
        rows.append({'Ticker': ticker, 'Price': None, 'Date': None})

# Save to CSV
df = pd.DataFrame(rows)
df.to_csv("yahoo_prices.csv", index=False)
