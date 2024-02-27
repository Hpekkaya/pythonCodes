"""
input range lower and upper
generate random number
calculate min numb of guess

initialize loop in range (repetitive guessing)
check the value bigger/smaller

messge with number of guess

"""

import math, random

lower, upper = 1, 100

count, guess = 0, 0

random_x = random.randint(lower, upper)

min_numb_of_guess = math.log((upper + lower) + 1, 2)

while guess != random_x:
    count += 1

    guess = int(input("Guess a number:- "))

    if guess == random_x:
        print(f"Conratulations you find the number at {count} th attempt")
        break

    elif guess > random_x:
        print("You guessed high number, guess lower")

    elif guess < random_x:
        print("You guessed low number, guess higher ")


if count > min_numb_of_guess:
    print(f"You found the number {count} th attemt")
