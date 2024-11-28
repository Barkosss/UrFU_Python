def create_counter(start):
    counter = start
    def increment():
        nonlocal counter
        counter += 1
        return counter
    return increment

def closure_pow2(start):
    counter = start
    def increment():
        nonlocal counter
        counter **= 2
        return counter
    return increment

def closure_str(string: str):
    def get_char(index: int) -> str:
        if 0 <= index < len(string):
            return string[index]
        else:
            return ''
    return get_char

def closure_sum(first: int):
    def add(second: int) -> int:
        return first + second
    return add

def closure_comparison(operator: str):
    def calculate(first: int, second: int) -> bool:
        if operator == "=":
            return first == second
        elif operator == ">":
            return first > second
        elif operator == "<":
            return first < second
        else:
            return False
    return calculate

def closure_del_str(string: str):
    def remove(index: int):
        if 0 <= index < len(string):
            return string[:index] + string[index + 1:]
        return string
    return remove

def closure_count_str(string: str):
    def count(char: string) -> int:
        return string.count(char)
    return count

def closure_check_bit(bit: int):
    def check_bit(num: int) -> bool:
        return (num & (1 << bit)) != 0
    return check_bit

def closure_list_pow(args: list):
    def compare(degree: int):
        for i in range(len(args)):
            args[i] **= degree
        return args
    return compare

def closure_list_del(args: list):
    def list_del(step: int):
        return [num for num in args if num % step != 0]
    return list_del
print(closure_list_del([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])(2))