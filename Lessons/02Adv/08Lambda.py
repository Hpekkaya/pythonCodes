# Lamda arguments:expressions

# Sorting

# add10 = lambda x: x + 10
# print(add10(5))

# mult = lambda x, y: x * y
# print(mult(5, 7))


# points2D = [(15, 2, 4), (1, 1, 5), (5, 6, -1), (10, 4, 2)]
# points2D_sorted = sorted(points2D)
# # sort with function x[0] as def in abv ln
# points2D_sorted_lmbd = sorted(points2D, key=lambda x: x[1])

# print(points2D)
# print((points2D_sorted))
# print((points2D_sorted_lmbd))

# points2D_sorted_lmbd = sorted(points2D, key=lambda x: x[2])
# print((points2D_sorted_lmbd))

# points2D_sorted_lmbd_sum = sorted(points2D, key=lambda x: x[1] + x[2])
# print((points2D_sorted_lmbd_sum))

# Functions ************************
# map (func, seq)  ********

# a = [1, 2, 3, 4, 5]
# b = map(lambda x: x * 2, a)

# print(list(b))

# c = [x * 2 for x in a]
# print(list(c))

# filter (func, seq)  ********

# a = [1, 2, 3, 4, 5, 6]
# b = filter(lambda x: x % 2 == 0, a)
# print(list(b))

# c = [x for x in a if x % 2 != 0]
# print(list(c))

# reduce (func, seq)  ********
from functools import reduce

a = [1, 2, 3, 4, 5]
produce_a = reduce(lambda x, y: x * y, a)
produce_b = reduce(lambda x, y: x + y, a)
produce_c = reduce(lambda x, y: x / y, a)


print(produce_a, produce_b, produce_c)


#
