#!/usr/bin/env python3
import re

try:
    import httpx
except ModuleNotFoundError:
    import pip
    pip.main(['install', '--quiet', 'httpx'])
    import httpx

# для обращения к веб-странице можно использовать примеры https://www.python-httpx.org

def get_content(name):
    """
    Функция возвращает содержимое вики-страницы name из русской Википедии.
    В случае ошибки загрузки или отсутствия страницы возвращается None.
    """
    content = httpx.get(f"https://ru.wikipedia.org/wiki/{name}").text
    return content


def extract_content(page):
    """
    Функция принимает на вход содержимое страницы и возвращает 2-элементный
    tuple, первый элемент - номер позиции, с которой начинается
    содержимое статьи, второй элемент — номер позиции, на котором заканчивается
    содержимое статьи.
    Если содержимое отсутствует, возвращается (0, 0).
    """
    start_content = page.find(re.findall(r"<div class=\"mw-content-ltr.*?>", page)[0])
    end_content = page.find(re.findall(r"<div id=\"mw-navigation\">", page)[0])
    return start_content, end_content


# ПРОБЛЕМНАЯ
def extract_links(page: str, begin: int, end: int):
    """
    Функция принимает на вход содержимое страницы и начало и конец интервала,
    задающего позицию содержимого статьи на странице и возвращает все имеющиеся
    ссылки на другие вики-страницы без повторений и с учётом регистра.
    """
    links = []
    for line in page[begin:end].splitlines():
        links.append(re.findall('"(?P<url>https?://[^\s]]+)"', line))
    print(links)
    return links


def find_chain(start: int, finish: int):
    """
    Функция принимает на вход название начальной и конечной статьи и возвращает
    список переходов, позволяющий добраться из начальной статьи в конечную.
    Первым элементом результата должен быть start, последним — finish.
    Если построить переходы невозможно, возвращается None.
    """
    pass


def main():
    content = get_content("Вулкан")
    indexs = extract_content(content)
    print(content)
    print(extract_links(content, indexs[0], indexs[1]))


if __name__ == '__main__':
    main()