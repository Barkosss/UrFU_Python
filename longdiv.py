#!/usr/bin/env python3

def long_division(dividend: int, divider: int) -> str:
    origDividend: int = dividend
    origDivider: int = divider

    negativeFlagDivider: int = 1 if (origDividend >= 0 and origDivider >= 0) or (origDividend < 0 and origDivider < 0) else -1
    divider: int = abs(divider)

    negativeFlagDividend: int = 1 if (origDividend >= 0 and origDivider >= 0) or (origDividend < 0 and origDivider < 0) else -1
    dividend: int = abs(dividend)

    strResult: str = ""
    countSpace: int = 0

    # If the dividend is less than the divider
    if dividend < divider:
        remains = dividend * 10
        fraction = ("-" if negativeFlagDividend == -1 else "") + "0."
        # We bring the dividend to such a number,
        # which will be greater than the divider
        while remains < divider:
            remains *= 10
            fraction += "0"

        while remains >= divider:
            quotient = remains // divider
            remains = remains % divider
            fraction += str(quotient)
            strResult += (" " * countSpace) + f"{negativeFlagDivider * quotient * divider} | {fraction}\n"
            countSpace = len(str(quotient * divider)) - len(str(remains))

            # If the dividend is less than the divider, then multiply by 10,
            # we also check the length so as not to fall into the period
            if remains < divider and len(fraction) < 20:
                remains *= 10
            else:
                break

        strResult += (" " * countSpace) + f"{negativeFlagDivider * remains}\n"
        return f'{origDividend} | {origDivider}\n{"-" * (len(str(dividend) + str(divider)) + 4)}\n' + strResult

    remains: int = dividend
    # If the dividend is greater than or equal to the divider
    while remains >= divider:
        quotient = remains // divider
        remains = remains % divider
        strResult += (" " * countSpace) + f"{negativeFlagDivider * quotient * divider} | {dividend // divider}\n"
        countSpace = len(str(quotient * divider)) - len(str(remains))

    strResult += (" " * countSpace) + f"{negativeFlagDivider * remains}\n"
    return f'{origDividend} | {origDivider}\n{"-" * (len(str(dividend) + str(divider)) + 4)}\n' + strResult


def main():
    # For tests
    arrValues = [[123, 123], [1, 1], [15, 3],
                 [3, 15], [12345, 25], [1234, 1423],
                 [87654532, 1], [24600, 123], [4567, 1234567],
                 [246001, 123], [123456789, 531], [425934261694251, 12345678],
                 [15, 2], [100, 33], [10000, 33],
                 [10, 20], [100, 400], [25, 400],
                 [10, 200], [10, 200], [100, 2000],
                 [10, 2000]]

    for dividend, divider in arrValues:
        print(long_division(dividend=dividend, divider=divider), end="\n")


if __name__ == '__main__':
    main()