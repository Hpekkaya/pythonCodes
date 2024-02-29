def romanToInt(s):
    # Map of Roman numerals to integers
    roman_map = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

    total = 0
    prev_value = 0

    for char in reversed(s):
        value = roman_map[char]  # Get the integer value for the Roman numeral
        if value < prev_value:
            # If the current value is less than the previous value, subtract it
            total -= value
        else:
            # Otherwise, add it to the total
            total += value
        prev_value = value  # Update the previous value

    return total


# Example usage
print(romanToInt("III"))  # Output: 3
print(romanToInt("IV"))  # Output: 4
print(romanToInt("IX"))  # Output: 9
print(romanToInt("LVIII"))  # Output: 58
print(romanToInt("MCMXCIV"))  # Output: 1994
