#
# def multiply(x, y):
#     if isinstance(x, (int, float)) and isinstance(y, (int, float)):
#         return round(x * y, 5)
#     else:
#         return x * y
#
# def no_of_letter(text):
#     return len(text)

def fizzbuzz(i):
    i = int(float(i))
    if i <= 0:
        return None
    elif i % 15 == 0:
        return "fizzbuzz"
    elif i % 5 == 0:
        return "buzz"
    elif i % 3 == 0:
        return "fizz"
    else:
        return i