from strategy import generate_signal, calculate_moving_average

print("Robin Agent starting...")

stocks = {
    "AAPL": 115,
    "TSLA": 105,
    "NVDA": 120,
    "MSFT": 110
    }

prices = [100,105,110,115,120]
moving_average = calculate_moving_average(prices)

for stock, price in stocks.items():
    signal = generate_signal(price, moving_average)

    print(f"Stock: {stock}")
    print(f"Price: ${price}")
    print(f"Moving Average: ${moving_average}")
    print(f"Signal: {signal}")
    print()