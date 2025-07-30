import yfinance as yf
import matplotlib.pyplot as plt

data = yf.download("AAPL", period="1mo")
data["Close"].plot(title="AAPL Stock Price")
plt.show()
