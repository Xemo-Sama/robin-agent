from strategy import generate_signal, calculate_moving_average
from risk import check_position_size

print("Robin Agent starting...")

portfolio_value = 10000
trade_amount = 500

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

    if signal == "BUY":
        risk_status = check_position_size(trade_amount, portfolio_value)
    else:
        risk_status = "NO TRADE"

    print(f"Stock: {stock}")
    print(f"Price: ${price}")
    print(f"Moving Average: ${moving_average}")
    print(f"Signal: {signal}")
    print(f"Risk Status: {risk_status}")
    print()