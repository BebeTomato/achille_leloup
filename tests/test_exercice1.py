import pytest
from exercice1 import Calculator

@pytest.fixture
def calculator():
    return Calculator()

def test_add(calculator):
    assert calculator.add(2, 3) == 5

def test_subtract(calculator):
    assert calculator.subtract(5, 2) == 3

def test_multiply(calculator):
    assert calculator.multiply(2, 4) == 8