import pytest

def test_add():
  assert add(2, 3) == 5
  assert add(-1, 1) == 0

def test_subtract():
  assert subtract(5, 2) == 3
  assert subtract(10, -5) == 15

def test_multiply():
  assert multiply(2, 3) == 6
  assert multiply(1, 0) == 0


def test_divide():
   with pytest.raises(ZeroDivisionError):
     divide(10, 0)
