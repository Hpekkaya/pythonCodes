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

rom_dic = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
def romanToInt(num):
    

    total = 0
    prev_value = 0

    for char in reversed(num):
        value = rom_dic[char]
        if value < prev_value:
            total -= value
        else:
            total += value
        prev_value = value

    return total

num="CCIV"
num=num.upper()

if (len(num)<1) and (len(num)>15):
    print("Please enter the length between 1-15")
if 