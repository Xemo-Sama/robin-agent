def generate_signal(price, moving_average):
    if moving_average is None:
        return "NO DATA"
    
    if price > moving_average:
        return "BUY"
    elif price < moving_average:
        return "WAIT"
    else:
        return "HOLD"

def  calculate_moving_average(prices):
    if len(prices) == 0:
        return None
    
    total = sum(prices)
    average = total/len(prices)
    return average
