#!/usr/bin/env python

import sys


def f0():
    raise BaseException


def f1():
    raise Exception


def f2():
    raise ArithmeticError


def f3():
    raise FloatingPointError


def f4():
    raise OverflowError


def f5():
    raise ZeroDivisionError


def f6():
    raise AssertionError


def f7():
    raise AttributeError


def f8():
    raise EnvironmentError


def f9():
    raise ImportError


def f10():
    raise LookupError


def f11():
    raise IndexError


def f12():
    raise KeyError


def f13():
    raise NameError


def f14():
    raise SyntaxError


def f15():
    raise ValueError


def f16():
    raise UnicodeError


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
