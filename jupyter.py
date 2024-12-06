def sized_cacher(size):
    def cacher(fn):
        dict_cacher = {}

        def wrapper(first: int, second: int) -> str:
            res = fn(first, second)
            if len(dict_cacher) > size:
                return str(res)

            if res not in dict_cacher:
                dict_cacher[res] = res
                return str(res)
            return f"cached: {res}"

        return wrapper

    return cacher


@sized_cacher(2)
def tsum(a, b):
    return a + b


assert (tsum(3, 2) == '5')
assert (tsum(3, 2) == 'cached: 5')
assert (tsum(2, 2) == '4')
assert (tsum(2, 2) == 'cached: 4')
assert (tsum(4, 4) == '8')
assert (tsum(4, 4) == '8')
print('Сразу +4 балла! Not bad!')
