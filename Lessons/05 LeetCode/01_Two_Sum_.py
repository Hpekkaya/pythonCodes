def twoSum(nums, target):
    # Initialize hash table
    prevMap = {}

    # Iterate through array
    for i, n in enumerate(nums):
        # Calculate complement
        diff = target - n
        if diff in prevMap:
            # Return indices if complement is found
            return [prevMap[diff], i]
        # Store index of the current element
        prevMap[n] = i


# Example usage
print(twoSum([2, 7, 11, 15], 26))
