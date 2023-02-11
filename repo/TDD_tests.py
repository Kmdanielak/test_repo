# import functions
from functions import *


# print(functions.multiply(5, 6))
# print(multiply(6, 6))


def test_multiply():
    assert multiply(5, 10) == 50
    assert multiply(100, 1.1) == 110
    assert multiply(1.5, 1.5) == 2.25
    assert multiply(0.000001, 100) == 0.0001