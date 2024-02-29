def is_palindrome(num):
    org_num = num  # Store the original number
    rev_num = 0  # Assign ReverseNumber 0 at the begining

    while num > 0:  # Reverse the original number (loop)
        digit = num % 10  # Get the last digit of the number
        num = num // 10  # Remove the last digit from the number
        rev_num = rev_num * 10 + digit  # Append the digit to reversed_num

    return org_num == rev_num  # Check if the original number is equal to its reverse


num = 22125
palindrome = is_palindrome(num)
print(f"{num} is palindrome : {palindrome}")
