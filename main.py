print("Robin Agent starting...")

stock = "AAPL"
price = 255.00
moving_average = 250.00

if price > moving_average:
    signal = "BUY"
else:
    signal = "WAIT"

print(f"Stock: {stock}")
print(f"Price: ${price}")
print(f"Moving Average: ${moving_average}")
print(f"Signal: {signal}")