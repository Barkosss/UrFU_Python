#!/usr/bin/env python3
from itertools import chain


def check_sex(name: str, male: bool = False, female: bool = False):
    if male:
        consonant_letters = ['б', 'в', 'г', 'д',
                             'ж', 'з', 'й', 'к',
                             'л', 'м', 'н', 'п',
                             'р', 'с', 'т', 'ф',
                             'х', 'ц', 'ч', 'ш', 'щ', 'ь']
        additional_names = ["никита", "илья", "данила", "лёва", "алехандро"]
        exceptions_names = ["любовь"]

        return True if ((name[-1] in consonant_letters or name.lower() in additional_names)
                        and name.lower() not in exceptions_names) else False

    if female:
        vowel_letters = ['а', 'е', 'ё', 'и', 'о', 'у', 'ы', 'э', 'ю', 'я']
        additional_names = ["любовь"]
        exceptions_names = ["никита", "илья", "данила", "лёва", "алехандро"]

        return True if ((name[-1] in vowel_letters or name.lower() in additional_names)
                        and name.lower() not in exceptions_names) else False


def make_stat(file_name: str) -> dict:
    """
    Функция вычисляет статистику по именам за каждый год с учётом пола.
    """
    with open(file_name, encoding="cp1251") as file:
        lines = file.readlines()
        years_names = {}

        for line in lines:
            # Find year
            if (start_index := line.find("<h3>")) and start_index != -1:
                end_index = line.find("</h3")
                year = line[start_index + 4:end_index]
                years_names[year] = {}

            # Find fullname
            if (start_index := line.find("/\">")) and start_index != -1:
                end_index = line.find("</a")
                full_name = line[start_index + 2:end_index]
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
    name_count = {}
    for year in stat.keys():
        for name, counter in stat[year].items():
            if name_count.get(name):
                name_count[name] += counter
            else:
                name_count[name] = counter

    general_stat_tuple = tuple(chain.from_iterable(name_count.items()))
    general_stat = [(general_stat_tuple[index], general_stat_tuple[index + 1])
                    for index in range(0, len(general_stat_tuple), 2)]
    general_stat.sort(key=lambda x: x[1], reverse=True)
    return general_stat


def extract_general_male(stat: dict) -> list:
    """
    Функция принимает на вход вычисленную статистику и выдаёт список tuple'ов
    (имя, количество) общей статистики для имён мальчиков.
    Список должен быть отсортирован по убыванию количества.
    """
    name_count = {}

    for year in stat.keys():
        for name, counter in stat[year].items():
            if check_sex(name, male=True):
                if name_count.get(name):
                    name_count[name] += counter
                else:
                    name_count[name] = counter

    general_male_tuple = tuple(chain.from_iterable(name_count.items()))
    general_male = [(general_male_tuple[index], general_male_tuple[index + 1])
                    for index in range(0, len(general_male_tuple), 2)]

    general_male.sort(key=lambda x: x[1], reverse=True)
    return general_male


def extract_general_female(stat: dict) -> list:
    """
    Функция принимает на вход вычисленную статистику и выдаёт список tuple'ов
    (имя, количество) общей статистики для имён девочек.
    Список должен быть отсортирован по убыванию количества.
    """
    name_count = {}

    for year in stat.keys():
        for name, counter in stat[year].items():
            if check_sex(name, female=True):
                if name_count.get(name):
                    name_count[name] += counter
                else:
                    name_count[name] = counter

    general_female_tuple = tuple(chain.from_iterable(name_count.items()))
    general_female = [(general_female_tuple[index], general_female_tuple[index + 1])
                      for index in range(0, len(general_female_tuple), 2)]

    general_female.sort(key=lambda x: x[1], reverse=True)
    return general_female


def extract_year(stat: dict, year: str) -> list:
    """
    Функция принимает на вход вычисленную статистику и год.
    Результат — список tuple'ов (имя, количество) общей статистики для всех
    имён в указанном году.
    Список должен быть отсортирован по убыванию количества.
    """
    if year not in stat.keys():
        return []

    stat_year = stat[year]
    extract_year_tuple = tuple(chain.from_iterable(stat_year.items()))
    extract_year_list = [(extract_year_tuple[index], int(extract_year_tuple[index + 1]))
                         for index in range(0, len(extract_year_tuple), 2)]

    extract_year_list.sort(key=lambda x: x[1], reverse=True)
    return extract_year_list


def extract_year_male(stat: dict, year: str) -> list:
    """
    Функция принимает на вход вычисленную статистику и год.
    Результат — список tuple'ов (имя, количество) общей статистики для всех
    имён мальчиков в указанном году.
    Список должен быть отсортирован по убыванию количества.
    """
    if year not in stat.keys():
        return []

    name_count = {}
    year_dict = stat[year]

    for name, counter in year_dict.items():
        if check_sex(name, male=True):
            if name_count.get(name):
                name_count[name] += counter
            else:
                name_count[name] = counter

    year_male_tuple = tuple(chain.from_iterable(name_count.items()))
    year_male = [(year_male_tuple[index], year_male_tuple[index + 1])
                 for index in range(0, len(year_male_tuple), 2)]
    year_male.sort(key=lambda x: x[1], reverse=True)
    return year_male


def extract_year_female(stat: dict, year: str) -> list:
    """
    Функция принимает на вход вычисленную статистику и год.
    Результат — список tuple'ов (имя, количество) общей статистики для всех
    имён девочек в указанном году.
    Список должен быть отсортирован по убыванию количества.
    """
    if year not in stat.keys():
        return []

    name_count = {}
    year_dict = stat[year]

    for name, counter in year_dict.items():
        if check_sex(name, female=True):
            if name_count.get(name):
                name_count[name] += counter
            else:
                name_count[name] = counter

    year_female_tuple = tuple(chain.from_iterable(name_count.items()))
    year_female = [(year_female_tuple[index], year_female_tuple[index + 1])
                   for index in range(0, len(year_female_tuple), 2)]
    year_female.sort(key=lambda x: x[1], reverse=True)
    return year_female


if __name__ == '__main__':
    pass
