import matplotlib.pyplot as plt

# Plot stock data
plt.figure(figsize=(10, 6))
plt.plot(tesla_data['Date'], tesla_data['Close'], label='Tesla Stock Price')
plt.title("Tesla Stock Prices")
plt.xlabel("Date")
plt.ylabel("Close Price")
plt.legend()
plt.show()
