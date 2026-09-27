from strategy import generate_signal, calculate_moving_average

print("Robin Agent starting...")

stocks = {
    "AAPL": { 
        "price": 115,
        "history": [100, 104, 108, 110, 112]
    },
    "TSLA": {
        "price": 250,
        "history": [270, 265, 260, 255, 252]
    },
    "NVDA": {
        "price": 190,
        "history": [170, 175, 180, 185, 188]
    },
    "MSFT": {
        "price": 420,
        "history": [420, 420, 420, 420, 420] 
    },
}

for stock, data in stocks.items():
    price = data["price"]
    prices = data["history"]

    moving_average = calculate_moving_average(prices)
    signal = generate_signal(price, moving_average)

    print(f"Stock: {stock}")
    print(f"Price: ${price}")
    print(f"Moving Average: ${moving_average}")
    print(f"Signal: {signal}")
    print()