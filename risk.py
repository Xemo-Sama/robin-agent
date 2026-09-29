def check_position_size(trade_amount,portfolio_value):
    max_position = portfolio_value * .10

    if trade_amount <= max_position:
        return "APPROVED"
    else:
        return "REJECTED"