#!/usr/bin/env python3
from urllib.request import urlopen
from requests import Response


def make_stat(filename):
    """
    Функция вычисляет статистику по именам за каждый год с учётом пола.
    """
    with open(filename) as file:
        lines = file.readlines()
        names = {}

        for line in lines:
            if (start_index := line.find("<h3>")) and start_index != -1:
                end_index = line.find("</h3")
                year = line[start_index+4:end_index]
                names[year] = {}

            if (start_index := line.find("/>")) and start_index != -1:
                end_index = line.find("</a")
                full_name = line[start_index+2:end_index]
                first_name = full_name.split(" ")[1]
                if names[year].get(first_name, False):
                    names[year][first_name] += 1
                else:
                    names[year][first_name] = 1


def extract_years(stat: dict) -> list:
    """
    Функция принимает на вход вычисленную статистику и выдаёт список годов,
    упорядоченный по возрастанию.
    """
    pass


def extract_general(stat: dict) -> tuple:
    """
    Функция принимает на вход вычисленную статистику и выдаёт список tuple'ов
    (имя, количество) общей статистики для всех имён.
    Список должен быть отсортирован по убыванию количества.
    """
    pass


def extract_general_male(stat: dict) -> tuple:
    """
    Функция принимает на вход вычисленную статистику и выдаёт список tuple'ов
    (имя, количество) общей статистики для имён мальчиков.
    Список должен быть отсортирован по убыванию количества.
    """
    pass


def extract_general_female(stat: dict) -> tuple:
    """
    Функция принимает на вход вычисленную статистику и выдаёт список tuple'ов
    (имя, количество) общей статистики для имён девочек.
    Список должен быть отсортирован по убыванию количества.
    """
    pass


def extract_year(stat: dict, year: int) -> tuple:
    """
    Функция принимает на вход вычисленную статистику и год.
    Результат — список tuple'ов (имя, количество) общей статистики для всех
    имён в указанном году.
    Список должен быть отсортирован по убыванию количества.
    """
    pass


def extract_year_male(stat: dict, year: int) -> tuple:
    """
    Функция принимает на вход вычисленную статистику и год.
    Результат — список tuple'ов (имя, количество) общей статистики для всех
    имён мальчиков в указанном году.
    Список должен быть отсортирован по убыванию количества.
    """
    pass


def extract_year_female(stat: dict, year: int) -> tuple:
    """
    Функция принимает на вход вычисленную статистику и год.
    Результат — список tuple'ов (имя, количество) общей статистики для всех
    имён девочек в указанном году.
    Список должен быть отсортирован по убыванию количества.
    """
    pass


if __name__ == '__main__':
    make_stat("CS _ home.html")