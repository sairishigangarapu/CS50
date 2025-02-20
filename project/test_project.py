import pytest
import tkinter as tk
from tkinter import END
import sys
from typing import Generator

# Import all functions from your calculator file
# Assuming the calculator file is named calculator.py in the same directory
from calculator import (
    input_num, input_decimal, input_pie, square,
    cal, reset, result, op1, op2, operation, res
)

@pytest.fixture
def setup_calculator() -> Generator[tuple[tk.Tk, tk.Entry], None, None]:
    """Fixture to set up the calculator environment before each test."""
    root = tk.Tk()
    tb1 = tk.Entry(root)
    # Make tb1 globally accessible as it's used in the calculator functions
    sys.modules['__main__'].tb1 = tb1

    # Reset global variables before each test
    reset()

    yield root, tb1

    # Cleanup after each test
    root.destroy()

def test_input_numbers(setup_calculator):
    _, tb1 = setup_calculator
    input_num('5')
    assert tb1.get() == '5'
    input_num('3')
    assert tb1.get() == '53'

def test_decimal_input(setup_calculator):
    _, tb1 = setup_calculator
    input_decimal('.')
    input_num('5')
    assert tb1.get() == '.5'

def test_pi_input(setup_calculator):
    _, tb1 = setup_calculator
    input_pie(3.14)
    assert tb1.get() == '3.14'

def test_square_function(setup_calculator):
    _, tb1 = setup_calculator
    tb1.insert(0, '5')
    square()
    assert tb1.get() == 'Ans = 25.0'

def test_addition(setup_calculator):
    _, tb1 = setup_calculator
    input_num('5')
    cal('+')
    tb1.delete(0, END)
    input_num('3')
    result()
    assert tb1.get() == 'Ans = 8.0'

def test_subtraction(setup_calculator):
    _, tb1 = setup_calculator
    input_num('10')
    cal('-')
    tb1.delete(0, END)
    input_num('4')
    result()
    assert tb1.get() == 'Ans = 6.0'

def test_multiplication(setup_calculator):
    _, tb1 = setup_calculator
    input_num('6')
    cal('*')
    tb1.delete(0, END)
    input_num('7')
    result()
    assert tb1.get() == 'Ans = 42.0'

def test_division(setup_calculator):
    _, tb1 = setup_calculator
    input_num('15')
    cal('/')
    tb1.delete(0, END)
    input_num('3')
    result()
    assert tb1.get() == 'Ans = 5.0'

def test_division_by_zero(setup_calculator):
    _, tb1 = setup_calculator
    input_num('15')
    cal('/')
    tb1.delete(0, END)
    input_num('0')
    result()
    assert tb1.get() == 'Ans = Division by Zero Error!'

def test_reset_function(setup_calculator):
    _, tb1 = setup_calculator
    input_num('123')
    reset()
    assert tb1.get() == ''
    assert op1 == ''
    assert op2 == ''
    assert operation == ''

def test_multiple_operations(setup_calculator):
    _, tb1 = setup_calculator
    input_num('5')
    cal('+')
    tb1.delete(0, END)
    input_num('3')
    cal('*')
    tb1.delete(0, END)
    input_num('2')
    result()
    assert tb1.get() == 'Ans = 16.0'

def test_decimal_calculations(setup_calculator):
    _, tb1 = setup_calculator
    input_num('5')
    input_decimal('.')
    input_num('5')
    cal('+')
    tb1.delete(0, END)
    input_num('2')
    input_decimal('.')
    input_num('5')
    result()
    assert tb1.get() == 'Ans = 8.0'
