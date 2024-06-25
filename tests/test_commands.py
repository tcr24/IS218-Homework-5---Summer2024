import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from HomeworkFive.command import AddCommand, SubtractCommand, MultiplyCommand, DivideCommand

def test_add_command():
    add = AddCommand()
    assert add.execute(1, 2) == 3

def test_subtract_command():
    subtract = SubtractCommand()
    assert subtract.execute(3, 1) == 2

def test_multiply_command():
    multiply = MultiplyCommand()
    assert multiply.execute(2, 3) == 6

def test_divide_command():
    divide = DivideCommand()
    assert divide.execute(6, 2) == 3
