def generate_signal(price, moving_average):
    if moving_average is None:
        return "NO DATA"
    percentage_difference = (price - moving_average) / moving_average
    
    if percentage_difference >= 0.02:
        return "BUY"
    elif percentage_difference <= -0.02:
        return "WAIT"
    else:
        return "HOLD"

def  calculate_moving_average(prices):
    if len(prices) == 0:
        return None
    
    total = sum(prices)
    average = total/len(prices)
    return average

