#!/usr/bin/env python

import sys
import math


def f0():
    x = 1 / 0


def f1():
    res = "false" * "false"


def f2():
    x = 1 / 0


def f3():
    raise FloatingPointError

def f4():
    bit_number = math.exp(10000)


def f5():
    x = 0 / 0


def f6():
    assert True == False


def f7():
    class User:
        def __init__(self, username, id):
            self.username = username
            self.id = id
    
    user = User("Barkos", 0)
    user_flag = user.flag


def f8():
    file = open("environmenterror.file", "r")


def f9():
    import BarkosLibrary


def f10():
    fruit_dict = {'apple': 120, 'banana': 50, 'pear': 10, 'manigo': 0}
    fruit_dict['blackberry']


def f11():
    array = [1, 2, 3, 4]
    element = array[10]


def f12():
    dict = {'a': 1, 'b': 2, 'c': 3}
    element = dict['error']


def f13():
    print(not_found_variable)


def f14():
    exec("if True print('Hello')")


def f15():
    int("false")


def f16():
    code = "Привет ошибка!"
    encode_code = code.encode("ascii")


def check_exception(f, exception):
    try:
        f()
    except exception:
        pass
    else:
        print("Bad luck, no exception caught: %s" % exception)
        sys.exit(1)


check_exception(f0, BaseException)
check_exception(f1, Exception)
check_exception(f2, ArithmeticError)
check_exception(f3, FloatingPointError)
check_exception(f4, OverflowError)
check_exception(f5, ZeroDivisionError)
check_exception(f6, AssertionError)
check_exception(f7, AttributeError)
check_exception(f8, EnvironmentError)
check_exception(f9, ImportError)
check_exception(f10, LookupError)
check_exception(f11, IndexError)
check_exception(f12, KeyError)
check_exception(f13, NameError)
check_exception(f14, SyntaxError)
check_exception(f15, ValueError)
check_exception(f16, UnicodeError)

print("Congratulations, you made it!")
