"""
Dict of Roman numerals to integers       
Generate total and prev values   
    
Generate for loop
    iterates through the Roman numeral string in reverse order
         
    Assign the first char RomanNumb of rev order to int value
        
    Check the current value whether less than previous  value
        if less substract it
        Otherwise, add it to the total        
    Update the previos value 

Const
len 1-15
only char
num in range(1,4000)
"""

rom_dict = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}


def romanToInt(num):

    total = 0
    prev_value = 0

    for char in reversed(num):
        value = rom_dict[char]
        if value < prev_value:
            total -= value
        else:
            total += value
        prev_value = value

    return total


def is_Roman(roman, valid_letters):

    for letter in roman:
        if letter not in valid_letters:
            return False

    return True


def is_valid_roman(roman):
    roman_numerals = {"I", "V", "X", "L", "C", "D", "M"}
    return all(char in roman_numerals for char in roman)


def find_invalid_romans(strings):
    invalid_romans = []
    for string in strings:
        if not is_valid_roman(string):
            invalid_romans.append(string)
    return invalid_romans


num = "CIVfr"
num = num.upper()

valid_roman = [str(key) for key in rom_dict.keys()]


if (len(num) < 1) and (len(num) > 15):
    print("Please enter the length between 1-15")
if is_Roman(num, valid_roman):
    print(romanToInt(num))
else:
    invalid_romans = find_invalid_romans(num)
    print("Please enter the ROMAN Number")
    print("Invalid Roman numerals:", list(invalid_romans))
