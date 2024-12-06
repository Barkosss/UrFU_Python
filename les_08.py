FILENAME = "shrek.png"  # файл для чтения
NEWFILENAME = "new_shrek.png"  # файл для записи


# Работа с бинарными данными
def read_and_write_bytes():
    # считываем файл в список image_data
    with open(FILENAME, "rb") as file:
        # print(f"изначальное положение указателя: {file.tell()}")  # изначальное положение указателя

        image_data = file.read()
        # print(f"конечное положение указателя: {file.tell()}")  # конечное положение указателя
        # print(file.seek(3))  # перемещаем указатель
        # print(file.tell())

    print(image_data)

    # запись выше считанных байт в новый файл
    with open(NEWFILENAME, "wb") as file:
        file.write(image_data)

    print(f"Файл {FILENAME} скопирован в {NEWFILENAME}")


import struct
from collections import namedtuple


def show_struct_1():
    my_string = "Hello, World!"

    # Преобразуем строку в байты (bytes) и упаковываем с использованием struct.pack
    format_string = '16s'
    packed_data = struct.pack(format_string, my_string.encode('utf-8'))
    print(packed_data)

    unpacked_data = struct.unpack(format_string, packed_data)  # кортеж
    print(unpacked_data[0].decode('utf-8'))


Info = namedtuple('Info', ['name', 'age', 'salary', 'height'])
from typing import NamedTuple


class Info2(NamedTuple):
    name: bytes
    age: int
    salary: int
    height: float

def show_struct_2():
    name = 'Shrek'
    age = 37
    salary = 1_000_000
    height = 2.15

    format_string = '<5sHIf'
    packed = struct.pack(format_string, name.encode('utf-8'), age, salary, height)
    print(packed)

    n, a, s, h = struct.unpack(format_string, packed)
    print(n.strip(b'\x00').decode('utf-8'), a, s, round(h, 2))
    info = Info(*struct.unpack(format_string, packed))
    info2 = Info2(*struct.unpack(format_string, packed))

    n, a, s, h = info2
    print(n, a, s, h)

    print(info)
    print(info2)


import pickle


def show_pickle_files():
    data = {
        'a': [1, 2.0, 3, 4 + 6j],
        'b': ("character string", b"byte string"),
        'c': {None, True, False}
    }

    with open('data.pickle', 'wb') as f:
        pickle.dump(data, f)

    with open('data.pickle', 'rb') as f:
        data_new = pickle.load(f)

    print(data_new)


def show_pickle_objects():
    data = {'name': 'Alice', 'age': 30, 'city': 'New York'}

    # Сериализуем словарь в бинарную строку с помощью pickle.dumps()
    serialized_data = pickle.dumps(data)

    # Выводим сериализованные данные
    print(serialized_data)
    deserialized_data = pickle.loads(serialized_data)
    print(deserialized_data)

show_pickle_objects()