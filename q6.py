# Plot stock data
plt.figure(figsize=(10, 6))
plt.plot(gamestop_data['Date'], gamestop_data['Close'], label='GameStop Stock Price', color='red')
plt.title("GameStop Stock Prices")
plt.xlabel("Date")
plt.ylabel("Close Price")
plt.legend()
plt.show()
