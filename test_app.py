from app import addition

def test_addition_positive():
    assert addition(2, 3) == 5

def test_addition_negative():
    assert addition(-1, 1) == 0

def test_addition_zero():
    assert addition(0, 0) == 0
    assert addition(0, 2) == 2

def test_addition_floats():
    assert addition(2.75, 4.75) == 7.5
