def two_sum(nums, target):
    complements = {}  # Store the compl and its index

    for i, num in enumerate(nums):  # Loop through the list of number
        complement = (
            target - num
        )  # Calc the compl by subs the curr numb from the target

        if complement in complements:  # Check if the compl is in the dict of compl
            return [complements[complement], i]  # if yes return cur ind and its comp
        complements[num] = 1  # store the curr numb and its ind

    return []  # if no solution return an empty list


nums = [2, 7, 18, 35]
target = 53

print(two_sum(nums, target))
