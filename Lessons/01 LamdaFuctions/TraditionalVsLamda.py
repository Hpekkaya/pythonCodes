
# Tadional Function
def count(x):
    y = x + 10
    return y

print("With Traditional Function")
print(count(10))
print()


# Lamda Function
x=lambda a,b,c:a+b+c+10

print("With Lamda Function")
print(x(5,10,15))

# Lamda with multiple parameters Function
x=lambda *args:sum(args)

print("With Lamda multiple parameters Function")
print(x(5,10,15,25))
