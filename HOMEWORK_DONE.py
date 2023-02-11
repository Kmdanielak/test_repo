# ex 1
# write Logger class taking and storing name in init
# with methods: info, warning, error, and critical
# each taking messafge argument and printing
# '{name of logger} {method name}: {message}'

class Logger:
    def __init__(self, name):
        self.name = name
    def info(self, message):
        print(f'{self.name} {self.info.__name__}: {message}')
    def warning(self, message):
        print(f'{self.name} {self.warning.__name__}: {message}')
    def error(self, message):
        print(f'{self.name} {self.error.__name__}: {message}')
    def critical(self, message):
        print(f'{self.name} {self.critical.__name__}: {message}')

# ex 2
# refactor Logger class to use only one '_log' method
# for prinitng messages

logger = Logger('simple_logger')
logger.info('hello')
logger.critical('world')
print()

# ex 3
# write functio taking iterable(list, tuple)
#     returning elements on odd indexes

def print_odd_indexes(arg):
    return arg[1::2]

print(print_odd_indexes([6,3,5,26,7,3]))
print(print_odd_indexes((6,3,5,26,7,3)))
print()

# ex 4
# write function checking if word is palindrome
#   palindrome is a word that read same from both
#   sides like 'level' and 'sos'

def is_palindrome(word):
    print(word == word[::-1])


is_palindrome('level')
is_palindrome('lelevel')
print()




# ex 5
# write function calculting bmi value and give
# option to round calculated result
# tip: use default argument
# more or less: bmi = weight_in_kg / height_in_m ** 2

def bmi(x, y, round_result=False):
    if round_result:
        bmi = round(x/(y ** 2))
    else:
        bmi = x / (y ** 2)
    return bmi

print('bmi', bmi(81, 1.76))
print('bmi', bmi(81, 1.76, True))
print('bmi', bmi(81, 1.76, round_result=True))
print()
