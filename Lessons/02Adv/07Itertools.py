#  itertools: product, permutations, combinations, accumulate, groupby, and infinite iterators

# from itertools import product

# a = [1, 2]
# b = [3, 4]
# my_prod = product(a, b)
# print(list(my_prod))

# my_prod = product(a, b, repeat=2)
# print(list(my_prod))

# from itertools import permutations, combinations

# a = [1, 2, 3]
# perm = permutations(a)
# print(list(perm))

# perm = permutations(a, 2)
# print(list(perm))

# a = [1, 2, 3, 4]
# comb = combinations(a, 2)
# print(list(comb))

# comb = permutations(a, 2)
# print(list(comb))

# from itertools import accumulate
# import operator

# a = [1, 2, 3, 4]
# acc = accumulate(a)
# print(a)
# print(list(acc))

# acc_opr = accumulate(a, func=operator.mul)
# print(list(acc_opr))

# a = [1, 2, 5, 3, 4]
# acc_max = accumulate(a, func=max)
# print(list(acc_max))


from itertools import groupby


# def smaller_than_3(x):
#     return x <= 3


# a = [0, 1, 2, 3, 4, 5, 6]
# print(a)


# group_obj = groupby(a, key=smaller_than_3)
# group_obj = groupby(a, key=lambda x: x <= 3)   #'nd alternative with Lamda

# for key, value in group_obj:
#     print(key, list(value))

# persons = [
#     {"name": "Hakan", "age": 54},
#     {"name": "Ahmet", "age": 52},
#     {"name": "Ahmet", "age": 19},
#     {"name": "Kerem", "age": 19},
# ]

# group_obj = groupby(persons, key=lambda x: x["age"])

# for key, value in group_obj:
#     print(key, list(value))

from itertools import count, cycle, repeat

a = [1, 2, 3]

# Count
# for i in count(10):
#     print(i, end=" ")
#     if i == 15:
#         break


# Cycle
# rep = 3
# seq_rep, seq_start = 0, 0
# seq_end = len(a) - 1


# for i in cycle(a):
#     if seq_start == 0:
#         print(f"Sequence {(seq_rep + 1)}")
#     print(i, end=" ")

#     if seq_start == seq_end:

#         if seq_rep >= rep:
#             break
#         else:
#             seq_start = 0
#             seq_rep += 1
#             print("\n")
#     else:
#         seq_start += 1

# Repeat


for i in repeat(a, 2):
    print(i, end=" ")

print("\n")

for i in repeat(5, 4):
    print(i, end=" ")

#
