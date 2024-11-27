import time

def delayed_output(second: int):
    def decorator(func):
        def wrapper(num: int):
            for n in func(num):
                time.sleep(second)
                #print(n, end=" ")
                yield n
        return wrapper
    return decorator

@delayed_output(1)
def countdown_generator(n: int):
    while n:
        yield n
        n -= 1

for i in countdown_generator(5):
    print(i, end=" ")