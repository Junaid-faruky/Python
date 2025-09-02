import yfinance as yf

stock = yf.Ticker("AAPL")
price = stock.history(period="1d")["Close"].iloc[-1]
print(f"Apple Stock Price: ${price:.2f}")
