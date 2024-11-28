import operator
import itertools

# Что такое итератор
class RangeIterator:
    def __init__(self, start, stop):
        self.start = start
        self.stop = stop
        self.curr = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.curr == self.stop:
            raise StopIteration

        self.curr = self.curr + 1
        return self.curr

# Что такое генератор
class RangeGenerator:
    def __init__(self, start, stop):
        self.start = start
        self.stop = stop
        self.curr = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.curr == self.stop:
            raise StopIteration
        self.curr = self.curr + 1
        return self.curr

    def send(self, value):
        if self.start <= value < self.stop:
            self.curr = value
            return value

        raise StopIteration


    def throw(self, value):
        pass

    def close(self):
        raise "end"

# send
def echo(value=None):
    print("Execution starts when next() is called for first time")
    try:
        while True:
            try:
                value = yield value
            except Exception as e:
                value = e # throw
    finally:
        print("Don't forget to close when close() is called")

generator = echo(1)
print(next(generator)) # 1
print(next(generator)) # None
print(generator.send(2)) # 2
print(generator.send(3)) # 3
print(generator.send(4)) # 4
generator.close()

# Примеры генераторной функции
def gen():
    yield 1
    return 2

def gen2():
    yield 1
    yield 2
    yield 3

b = gen2()
print(next(b))
print(next(b))
print(next(b))
print(next(b))

# yield from
def gen3():
    yield from range(1, 3)
    for i in range(1, 3):
        yield i

for i in gen3():
    print(i)

# Примеры генераторного выражения
def get_expression():
    a = [i for i in range(5)]
    b = (i for i in range(5))

    for i in a:
        print(i)

    for i in b:
        print(i)

get_expression()

# zip

# sum

# all (= and)
def get_all():
    a = [0, 1, 2, 3]
    print(all(a)) # False (из-за 0 в массиве)

# item

# any
