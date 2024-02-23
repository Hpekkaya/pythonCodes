data = [1, 2, -4, -3]

# Iterate with enumerate(x) instead or range(len(x))

for idx, num in enumerate(data):
    if num < 0:
        data[idx] = 0

# print(data)

# Use list comprehension instead of raw for loops

squares = []
for i in range(10):
    squares.append(i**i)
# print(squares)


squares = [i**i for i in range(10)]
# print(squares)
