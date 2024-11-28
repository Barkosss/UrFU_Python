def pow_list_result(func):
    def multi(arr):
        result = func(arr)
        return result ** 2
    return multi


@pow_list_result
def sum_list(arr):
    return sum(arr)

from math import sqrt
def sqrt_list_result(func):
    def compare(num: int):
        return sqrt(func(num))
    return compare

@sqrt_list_result
def max_number(arr):
    return max(arr)

def upcase_result(func):
    def upper(string: str):
        return func(string).upper()
    return upper

@upcase_result
def reverse_str(string: str):
    return string[::-1]

def check_bit(func):
    def bit(num: int):
        return func(num) + 10 if (num >> 2) & 1 else func(num) - 5
    return bit

@check_bit
def pow3(num: int):
    return num ** 3


def str_case_result(func):
    def compare(string, char):
        result = func(string, char)
        mid = len(result) // 2

        return result[:mid].upper() + result[mid:mid+1] + result[mid+1:].lower()

    return compare


@str_case_result
def del_str(string, char):
    return string.replace(char, "")


def celsius(func):
    def wrapper(fahrenheit):
        return (func(fahrenheit) - 32) * 5 / 9
    return wrapper

@celsius
def temperature_fahrenheit(fahrenheit):
    return fahrenheit


def check_type(func):
    def checker_int(value):
        if isinstance(value, int):
            return func(value) * 2
        else:
            return None
    return checker_int

@check_type
def reply_int(value):
    return value


def mul_result(N: int = 2):
    def decorator(func):
        def wrapper(first, second):
            return func(first, second) * N
        return wrapper
    return decorator

@mul_result()
def add(first, second):
    return first + second