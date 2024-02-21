# Set is a collection which is unordered, changeable*, and unindexed. No duplicate members.

# my_set = {1,3,5,38,5,3}
# print(my_set) # No duplicate members.

# my_set = set("Hello")
# print(my_set)

# my_set = set()
# print(type(my_set))
# print(my_set)

# my_set.add(1)
# my_set.add(7)
# my_set.add(8)
# my_set.add(5)

# print(my_set)

# my_set.remove(3) #unindexed only values returns KeyError:
# print(my_set)

# my_set.clear()

# my_set.pop() #pop the last value
# print(my_set)

# Loops in Set
# for x in my_set:
#     print(x)


# Check
# if 5 in my_set:
#     print("Yes", 5,"in Set")

# odds ={1,3,5,7,9}
# evens={0,2,4,6,8}
# primes={2,3,5,7}

# u=odds.union(evens)
# print(u)
# print(odds,evens)

# i=odds.intersection(evens)
# i1 = odds.intersection(primes)
# print(i,i1)

set_A = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
set_B = {0,  3, 4,  6, 7,  9, 10,12,14}

# dif = set_A.difference(set_B)
# print("dif", dif, set_A,set_B)

# dif1 = set_B.difference(set_A)
# print("dif1", dif1, set_A,set_B)

# dif2 = set_B.symmetric_difference(set_A)
# print("dif2", dif2, set_A,set_B)

dif3 = set_B.intersection(set_A)
print("dif3", dif3, set_A,set_B)

set_A.intersection_update(set_B)
print("dif4", set_A,set_B)


