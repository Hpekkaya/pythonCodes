import sys


def two_sum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    # Dictionary to store the complement and its index
    complements = {}
    # Loop through the list of numbers
    num_enum = list(enumerate(nums))
    for i, num in enumerate(nums):
        # Calculate the complement by subtracting the current number from the target
        complement = target - num
        # Check if the complement is in the dictionary
        if complement in complements:
            # If yes, return the current index and the index of the complement
            return [complements[complement], i]
        # Store the current number along with its index in the dictionary
        complements[num] = i
    # If no solution is found, return an empty list (or raise an exception)
    return []


from timeit import default_timer as timer

start = timer()

# Example usage
nums = [2, 7, 11, 15, 18, 35]
target = 26
print(two_sum(nums, target))

stop = timer()
time = stop - start
print(time * 1000000)
