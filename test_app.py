from app import addition, subtraction, multiplication, division

def test_addition():
    assert addition(3, 3) == 6

def test_subtraction():
    assert subtraction(7, 3) == 4

def test_multiplication():
    assert multiplication(9, 3) == 27

def test_division():
    assert division(30, 2) == 15
