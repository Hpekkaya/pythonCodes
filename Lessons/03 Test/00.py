data = [1, 2, -4, -3]

for i, num in enumerate(data):
    if num < 0:
        data[i] = 0

print(data)
