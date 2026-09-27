def generate_signal(price, moving_average):
    if price > moving_average:
        return "BUY"
    elif price < moving_average:
        return "WAIT"
    else:
        return "HOLD"
    
print("Robin Agent starting...")

stock = input("Enter stock symbol: ")
price = float(input("Enter current price: "))
moving_average = float(input("Enter moving average: "))

signal = generate_signal(price, moving_average)

print(f"Stock: {stock}")
print(f"Price: ${price}")
print(f"Moving Average: ${moving_average}")
print(f"Signal: {signal}")

