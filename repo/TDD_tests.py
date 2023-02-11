# import functions
from functions import *


# print(functions.multiply(5, 6))
# print(multiply(6, 6))


def test_multiply():
    assert multiply(5, 10) == 50
    assert multiply(100, 1.1) == 110
    assert multiply(1.5, 1.5) == 2.25
    assert multiply(0.000001, 100) == 0.0001
    assert multiply("mama", 3) == "mamamamamama"
    assert multiply(None, 5) == None
    # nie odpowiedzieliśmy na ten warunek

def test_number_of_letters():
    assert no_of_letter("mama") == 4
    assert no_of_letter("mama.tata") == 8
    # nie odpowiedzieliśmy na ten warunek