from strategy import generate_signal, calculate_moving_average

def test_buy_signal():
    result = generate_signal(120,100)
    assert result == "BUY"

def test_wait_signal():
    result = generate_signal(90,100)
    assert result == "WAIT"

def test_hold_signal():
    result = generate_signal(100,100)
    assert result == "HOLD"

def test_nodata_signal():
    result = generate_signal(100,None)
    assert result == "NO DATA"

def test_moving_average():
    prices = [100,105,110,115,120]
    result = calculate_moving_average(prices)
    assert result == 110

def test_above_threshold():
    result = generate_signal(103,100)
    assert result == "BUY"

def test_below_threshold():
    result = generate_signal(97,100)
    assert result == "WAIT"

def test_above_hold():
    result = generate_signal(101,100)
    assert result == "HOLD"

def test_below_hold():
    result = generate_signal(99,100)
    assert result == "HOLD"

def test_buy_threshold():
    result = generate_signal(102,100)
    assert result == "BUY"

def test_hold_threshold():
    result = generate_signal(98,100)
    assert result == "WAIT"