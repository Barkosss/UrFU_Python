#!/usr/bin/env python3

def long_division(dividend: int, divider: int) -> str:
    if dividend == 0 or divider == 0:
        return f'{dividend} | {divider}\n{"-" * (len(str(dividend) + str(divider)) + 4)}\n0\n'

    orig_dividend: int = dividend
    orig_divider: int = divider

    negative_flag_divider: int
    if (orig_dividend >= 0 and orig_divider >= 0) or (orig_dividend < 0 and orig_divider < 0):
        negative_flag_divider = 1
    else:
        negative_flag_divider = -1

    divider: int = abs(divider)

    negative_flag_dividend: int
    if (orig_dividend >= 0 and orig_divider >= 0) or (orig_dividend < 0 and orig_divider < 0):
        negative_flag_dividend = 1
    else:
        negative_flag_dividend = -1

    dividend: int = abs(dividend)

    result: str = ""
    count_space: int = 0

    # If the dividend is less than the divider
    if dividend < divider:
        remains = dividend * 10
        fraction = ("-" if negative_flag_dividend == -1 else "") + "0."
        # We bring the dividend to such a number,
        # which will be greater than the divider
        while remains < divider:
            remains *= 10
            fraction += "0"

        while remains >= divider:
            quotient = remains // divider
            remains = remains % divider
            fraction += str(quotient)
            result += (" " * count_space) + f"{quotient * divider} | {fraction}\n"
            count_space = len(str(quotient * divider)) - len(str(remains))

            # If the dividend is less than the divider, then multiply by 10,
            # we also check the length so as not to fall into the period
            if remains < divider and len(fraction) < 20:
                remains *= 10
            else:
                break

        result += (" " * count_space) + f"{negative_flag_divider * remains}\n"
        return f'{orig_dividend} | {orig_divider}\n{"-" * (len(str(dividend) + str(divider)) + 4)}\n' + result

    remains: int = dividend
    # If the dividend is greater than or equal to the divider
    while remains >= divider:
        quotient = remains // divider
        remains = remains % divider
        result += (" " * count_space) + f"{quotient * divider} | {dividend // divider}\n"
        count_space = len(str(quotient * divider)) - len(str(remains))

    result += (" " * count_space) + f"{negative_flag_divider * remains}\n"
    return f'{orig_dividend} | {orig_divider}\n{"-" * (len(str(dividend) + str(divider)) + 4)}\n' + result


def main():
    # For tests
    arr_values = [[123, 123], [1, 1], [15, 3],
                 [3, 15], [12345, 25], [1234, 1423],
                 [87654532, 1], [24600, 123], [4567, 1234567],
                 [246001, 123], [123456789, 531], [425934261694251, 12345678],
                 [15, 2], [100, 33], [10000, 33],
                 [10, 20], [100, 400], [25, 400],
                 [10, 200], [10, 200], [100, -2000],
                 [-10, 2000], [10, 0], [0, 10]]

    for dividend, divider in arr_values:
        print(long_division(dividend=dividend, divider=divider), end="\n")


if __name__ == '__main__':
    main()