def is_palindrome(number):
    original_number = number
    reversed_number = 0

    while number > 0:
        digit = number % 10  # Get the last digit of the number
        number = number // 10  # Remove the last digit from the original number
        reversed_number = reversed_number * 10 + digit  # Build the reversed number

    return original_number == reversed_number


min = -(2**31)
max = -min - 1
number = 251523

if (number >= min) and (number <= max):
    if is_palindrome(number):
        print(
            f"{number} is Palindrome ",
        )  # True
    else:
        print(
            f"{number} isnot Palindrome",
        )  # False
else:
    print(f"{number} is not in range")
