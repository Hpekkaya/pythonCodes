import functools


add = functools.reduce(lambda x, y: x + y, range(1, 11))


print(add)
