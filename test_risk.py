from risk import check_position_size

def test_five_risk():
    result = check_position_size(500,10000)
    assert result == "APPROVED"

def test_ten_risk():
    result = check_position_size(1000,10000)
    assert result == "APPROVED"  

def test_over_risk():
    result = check_position_size(1500,10000)
    assert result == "REJECTED"