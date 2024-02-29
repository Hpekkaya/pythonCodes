data = [1, 2, -6, -9, -4, -3, -5]

# 1 Iterate with enumerate(x) instead or range(len(x))

for idx, num in enumerate(data):
    if num < 0:
        data[idx] = -num

print(data)

# 2 Use list comprehension instead of raw for loops

squares = []
for i in range(10):
    squares.append(i**i)
# print(squares)


# squares = [i**i for i in range(10)]
# print(squares)

# 3 Sort Complex itearables
sorted_data = sorted(data)
# print(sorted_data)

data = [
    {"name": "Hakan", "age": 54},
    {"name": "Mehmet", "age": 51},
    {"name": "Hatice", "age": 48},
    {"name": "Fatih", "age": 44},
]

sorted_data = sorted(data, key=lambda x: x["name"])
# print(sorted_data)

# 4 Store Uniq values with sets

# my_list = [1, 2, 3, 4, 2, 5, 4, 8, 7, 3, 2, 2]
# my_list = sorted(my_list)
# print(my_list)
# my_set = set(my_list)
# print(my_set)

# 5 Save Memory with generators () when we compare list[]

# import sys
# Bad
# my_list = [i for i in range(1, 10000, 2)]
# print(sum(my_list))

# size = sys.getsizeof(my_list), "bytes"
# print(size)

# Good
# my_gen = (i for i in range(1, 10000, 2))
# print(sum(my_gen))

# size = sys.getsizeof(my_gen), "bytes"
# print(size)

# 6 Define default values in Dictionaries with .get() and .setdefault

# my_dict = {"item": "footbal", "price": 10}
# count = my_dict.get("count", 0)
# print(count)

# count = my_dict.setdefault("item", 0)
# print(count)
# print(my_dict)

# 7 Count hashable objects with collections

# from collections import Counter

# my_list = [10, 10, 10, 5, 5, 2, 9, 9, 9, 9, 9, 9, 9, 3, 3, 3, 3, 3, 3]
# counter = Counter(my_list)
# print(counter)

# most_common = counter.most_common(2)
# print(most_common)

# 8 Format strings with f strings
# name = "Hakan"
# my_string = f"Hello {name}"
# print(my_string)

# i = 10
# print(f"{i} squarred is {i*i}")

# 9 concat string with .join()

# list_of_string = ["Hello", "my", "friends"]

# my_string = ", ".join(list_of_string)
# print(my_string)

# 10 Merge two dictionaries
d1 = {"name": "Hakan", "age": 54}
d2 = {"name": "Mehmet", "city": "Istanbul"}

merged_dict = {**d1, **d2}
print(merged_dict)
