from strategy import generate_signal, calculate_moving_average

print("Robin Agent starting...")

stock = input("Enter stock symbol: ")
price = float(input("Enter current price: "))
prices = [100,105,110,115,120]
moving_average = calculate_moving_average(prices)
signal = generate_signal(price, moving_average)

print(f"Stock: {stock}")
print(f"Price: ${price}")
print(f"Moving Average: ${moving_average}")
print(f"Signal: {signal}")

