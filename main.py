print("Robin Agent starting...")

stock = input("Enter stock symbol: ")
price = float(input("Enter current price: "))
moving_average = float(input("Enter moving average: "))

if price > moving_average:
    signal = "BUY"
elif price < moving_average:
    signal = "WAIT"
else:
    signal = "HOLD"

print(f"Stock: {stock}")
print(f"Price: ${price}")
print(f"Moving Average: ${moving_average}")
print(f"Signal: {signal}")