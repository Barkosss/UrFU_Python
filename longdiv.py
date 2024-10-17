#!/usr/bin/env python3
from itertools import repeat, count


def long_division(dividend: int, divider: int) -> str:
    strResult = ""; countSpace = 0
    """
    Вернуть строку с процедурой деления «уголком» чисел dividend и divider.
    Формат вывода приведён на примерах ниже.

    Примеры:
        12345÷25
    12345|25
    100  |493
     234
     225
       95
       75
       20

        1234÷1423
    1234|1423
    1234|0

        24600÷123
    24600|123
    246  |200
      0

        246001÷123
    246001|123
    246   |2000
         1
    """

    remains = dividend
    while remains >= divider:
        quotient = remains // divider
        remains = remains % divider
        strResult += f"{quotient}\n"
        countSpace += 1
    strResult += f"{remains}\n"
    return f'{dividend} ÷ {divider}\n{dividend} |{divider}\n' +  strResult


def main():
    arrValues = [[123, 123], [1, 1], [15, 3], [3, 15], [12345, 25], [1234, 1423], [87654532, 1], [24600, 123],
           [4567, 1234567], [246001, 123], [123456789, 531], [425934261694251, 12345678]]

    for dividend, divider in arrValues:
        print(long_division(dividend=dividend, divider=divider))
        print()


if __name__ == '__main__':
    main()