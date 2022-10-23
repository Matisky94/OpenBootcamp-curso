import math


def is_armstrong_number(number):
    number_of_digits = get_number_of_digits(number)
    list_of_digits = get_each_digit(number, number_of_digits)
    result = sum(x**number_of_digits for x in list_of_digits)
    print(result)
    return result

def get_number_of_digits(number):
    i = 0
    while number > 0:
        number = math.trunc(number / 10)
        i += 1
    print("num of digits:", i)
    return i
    
def get_each_digit(number, number_of_digits):
    list_of_digits = []
    while number_of_digits > 0:
        list_of_digits.append(number % 10)
        number = math.trunc(number / 10)
        number_of_digits -= 1
    print("list of digits:", list_of_digits)
    return list_of_digits

is_armstrong_number(153)