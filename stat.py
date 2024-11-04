#!/usr/bin/env python3
from itertools import chain


def make_stat(file_name: str) -> dict:
    """
    Функция вычисляет статистику по именам за каждый год с учётом пола.
    """
    with open(file_name) as file:
        lines = file.readlines()
        years_names = {}

        for line in lines:
            # Find year
            if (start_index := line.find("<h3>")) and start_index != -1:
                end_index = line.find("</h3")
                year = line[start_index+4:end_index]
                years_names[year] = {}

            # Find fullname
            if (start_index := line.find("/\">")) and start_index != -1:
                end_index = line.find("</a")
                full_name = line[start_index+2:end_index]
                first_name = full_name.split(" ")[1]
                if years_names[year].get(first_name, False):
                    years_names[year][first_name] += 1
                else:
                    years_names[year][first_name] = 1

        return years_names


def extract_years(stat: dict) -> list:
    """
    Функция принимает на вход вычисленную статистику и выдаёт список годов,
    упорядоченный по возрастанию.
    """

    return sorted(stat.keys())


def extract_general(stat: dict) -> list:

    """
    Функция принимает на вход вычисленную статистику и выдаёт список tuple'ов
    (имя, количество) общей статистики для всех имён.
    Список должен быть отсортирован по убыванию количества.
    """
    general_stat: list = []
    # ...
    # ...
    # ...
    print(general_stat)
    return general_stat


def extract_general_male(stat: dict) -> list:
    """
    Функция принимает на вход вычисленную статистику и выдаёт список tuple'ов
    (имя, количество) общей статистики для имён мальчиков.
    Список должен быть отсортирован по убыванию количества.
    """
    consonant_letters = ['б', 'в', 'г', 'д',
                         'ж', 'з', 'й', 'к',
                         'л', 'м', 'н', 'п',
                         'р', 'с', 'т', 'ф',
                         'х', 'ц', 'ч', 'ш', 'щ']
    exceptions_names = ["никита"]
    name_count = {}

    for year in stat.keys():
        for name, counter in stat[year].items():
            if name[-1] in consonant_letters or name.lower() in exceptions_names:
                if name_count.get(name):
                    name_count[name] += counter
                else:
                    name_count[name] = 1

    general_male_tuple = tuple(chain.from_iterable(name_count.items()))
    general_male = [(general_male_tuple[index], general_male_tuple[index + 1])
                    for index in range(0, len(general_male_tuple), 2)]

    print(general_male)
    return general_male


def extract_general_female(stat: dict) -> list:
    """
    Функция принимает на вход вычисленную статистику и выдаёт список tuple'ов
    (имя, количество) общей статистики для имён девочек.
    Список должен быть отсортирован по убыванию количества.
    """
    vowel_letters = ['а, е, ё, и, о, у, ы, э, ю, я']
    exceptions_names = []
    name_count = {}

    for year in stat.keys():
        for name, counter in stat[year].items():
            if name[-1] in vowel_letters or name.lower() in exceptions_names:
                if name_count.get(name):
                    name_count[name] += counter
                else:
                    name_count[name] = 1

    general_female_tuple = tuple(chain.from_iterable(name_count.items()))
    general_female = [(general_female_tuple[index], general_female_tuple[index + 1])
                      for index in range(0, len(general_female_tuple), 2)]

    print(general_female)
    return general_female


def extract_year(stat: dict, year: int) -> list:
    """
    Функция принимает на вход вычисленную статистику и год.
    Результат — список tuple'ов (имя, количество) общей статистики для всех
    имён в указанном году.
    Список должен быть отсортирован по убыванию количества.
    """
    pass


def extract_year_male(stat: dict, year: int) -> list:
    """
    Функция принимает на вход вычисленную статистику и год.
    Результат — список tuple'ов (имя, количество) общей статистики для всех
    имён мальчиков в указанном году.
    Список должен быть отсортирован по убыванию количества.
    """
    pass


def extract_year_female(stat: dict, year: int) -> list:
    """
    Функция принимает на вход вычисленную статистику и год.
    Результат — список tuple'ов (имя, количество) общей статистики для всех
    имён девочек в указанном году.
    Список должен быть отсортирован по убыванию количества.
    """
    pass


if __name__ == '__main__':
    filename: str = "stat.html"
    stats: dict = make_stat(filename)
    stat_extract_years: list = extract_years(stats)
    extract_general(stats)
    extract_general_male(stats)