import unittest
from typing import Any


# Написать list comprehension, который принимает список слов
# и возвращает эти слова перевернутыми в верхнем регистре, только если их длина больше и равна 3

# Пример:
# Вход: ['q', 'aa', 'bas', 'kuba']
# Выход: ['SAB', 'ABUK']
def get_upper_words(words: list[str]) -> list[str]:
    arr_upper_words = []
    for word in words:
        if len(word) >= 3:
            arr_upper_words.append(word[::-1].upper())
    return arr_upper_words  # ЗДЕСЬ МОГ БЫ БЫТЬ ВАШ КОД


# Написать генераторную функцию (yield), которая принимает на вход список и зацикливает его значения
# Каждую итерацию удаляется первое значение

# Пример:
# Вход: [1, 2, 3, 4]
# Выход: -> 1, 2, 3, 4, 2, 3, 4, 3, 4, 4
def cycle_generator(collection: list[Any]):
    for start in range(len(collection)):
        for num in range(start, len(collection)):
            yield collection[num]


# Написать генераторную функцию, которой через send (см. test_sum_generator) посылаются значения
# Функция возвращает общую сумму всех отправленных значений

# Пример:
# Вход: -> 1, 2, 3
# Выход: -> 1, 3, 6
def sum_generator():
    total = 0
    while True:
        num = yield total
        if num is None:
            continue
        total += num



class TestStatistics(unittest.TestCase):
    def test_get_upper_words(self):
        words = ['q', 'aa', 'bas', 'kuba']
        actual = get_upper_words(words)
        expected = ['SAB', 'ABUK']
        self.assertEqual(actual, expected)

    def test_cycle_generator(self):
        data = [1, 2, 3, 4]
        actual = list(cycle_generator(data))
        expected = [1, 2, 3, 4, 2, 3, 4, 3, 4, 4]
        self.assertEqual(actual, expected)

    def test_sum_generator(self):
        gen = sum_generator()
        # инициализируем генератор
        next(gen)

        actual = []

        # Отправляем числа в генератор и выводим сумму после каждой итерации
        for value in [1, 2, 3, 4, 5]:
            current_sum = gen.send(value)
            actual.append(current_sum)

        expected = [1, 3, 6, 10, 15]
        self.assertEqual(actual, expected)
