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

# sorted_data = sorted(data, key=lambda x: x["age"])
# print(sorted_data)
