def countdown(n):
    # Base case: if n is 0, stop the recursion
    if n == 0:
        print(n)
    else:
        # Print the current value of n
        print(n, end=" ")
        # Call the countdown function with n-1
        countdown(n - 1)


# Call the countdown function with an initial value of 5
countdown(5)
