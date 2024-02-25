def is_polindrome(number):
    org_number = str(number)
    rev_number = str(org_number[::-1])
    return org_number == rev_number


min = -(2**31)
max = -min - 1
number = 2**32


if number >= min and number <= max:
    if is_polindrome(number):
        print(f"Yes {number} is polindrome")
    else:
        print(f"No {number} isnot polindrome")
else:
    print(f"{number} is not in range")
