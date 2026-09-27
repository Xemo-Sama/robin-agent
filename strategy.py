def generate_signal(price, moving_average):
    if price > moving_average:
        return "BUY"
    elif price < moving_average:
        return "WAIT"
    else:
        return "HOLD"
   