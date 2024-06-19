import pytest
from HomeworkFive.command import AddCommand, SubtractCommand, MultiplyCommand, DivideCommand

def test_add():
    cmd = AddCommand()
    assert cmd.execute(1, 2, 3) == 6
    assert cmd.execute(0, 0) == 0

def test_subtract():
    cmd = SubtractCommand()
    assert cmd.execute(10, 5) == 5
    with pytest.raises(ValueError):
        cmd.execute(10)

def test_multiply():
    cmd = MultiplyCommand()
    assert cmd.execute(2, 3) == 6
    assert cmd.execute(0, 10) == 0

def test_divide():
    cmd = DivideCommand()
    assert cmd.execute(10, 2) == 5
    with pytest.raises(ValueError):
        cmd.execute(10, 0)
