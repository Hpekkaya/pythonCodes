"""
Inputs for generating random number in range
generate a random number,
Initializing the number of guesses for calculation of minimum number of guesses depends upon range

Initialize the loop in the range of minumum guess
    Take the guessing number as input
    Condition testing If Guessing is more than required guesses,
shows output.

"""

import math, random


def check_guess(g, r):
    if g < r:
        return -1
    elif g > r:
        return +1
    elif g == r:
        return 0


lower, higher = 0, 100

random_x = int(random.randint(lower, higher))

count = 0

min_guess = math.log((higher - lower + 1), 2)
min_guess = math.ceil(min_guess)

while count < min_guess:
    count += 1
    guess = int(input(f"Enter your {count}. guess :"))

    result = check_guess(guess, random_x)
    if result == 0:
        print(f"Congratulations you find at {count} attemt")
        break

    elif result == 1:
        print(f"Your guess is high, guess lower")

    elif result == -1:
        print(f"Your guess is low, guess higher")

if count > min_guess:
    print(f"\nThe number is {random_x}")
    print("\tBetter Luck Next time")
