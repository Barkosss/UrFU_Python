class Book:

    def __init__(self, title: str, author: str, genre: str):
        self.title = title
        self.author = author
        self.genre = genre


class Library:

    def __init__(self):
        self.library:list[Book] = []

    def add_book(self, book: Book):
        self.library.append(book)

    def remove_book(self, title:str):
        for index, book in enumerate(self.library):
            if title == book.title:
                self.library.remove(book)
                break
        else:
            print(f"Book \"{title}\" is not found")

    def __str__(self):
        result = []
        for book in self.library:
            result.append(f"Title: {book.title},\nAuthor: {book.author},\nGenre: {book.genre}\n")

        return "\n".join(result)

    def __len__(self):
        return len(self.library)


# Пример использования

# Создаем экземпляр класса Library
library = Library()

# Создаем несколько экземпляров класса Book
book1 = Book(title="Python Programming", author="John Smith", genre="Programming")
book2 = Book(title="Introduction to AI", author="Alice Johnson", genre="Artificial Intelligence")

# Добавляем книги в библиотеку
library.add_book(book1)
library.add_book(book2)

# Получаем количество всех книг
print(len(library)) # 2
# Выводим список всех книг в библиотеке
print(str(library))
# Python Programming by John Smith (Programming)
# Introduction to AI by Alice Johnson (Artificial Intelligence)


# Удаляем одну из книг
library.remove_book("Python Programming")
# Удаляем несуществующую
library.remove_book("Billie Eilish")  # Данной книги не существует

# Получаем количество всех книг
print(len(library)) # 1
# Выводим список всех книг в библиотеке
print(str(library))
# Introduction to AI by Alice Johnson (Artificial Intelligence)