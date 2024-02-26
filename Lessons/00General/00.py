# A simple Python function to check
# whether x is even or odd


def evenOdd(x):
    """Function to check if the number is even or odd"""

    if x % 2 == 0:
        return "even"
    else:
        return "odd"


# Driver code to call the function
print(evenOdd.__doc__)

y = 75
x = evenOdd(y)
print(f"The number {y:.2f} is {x}")
