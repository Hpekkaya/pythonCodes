def twoSum(nums, target):
    # Initialize hash table
    new_dict = {}
    my_dict = enumerate(nums)
    # Iterate through array
    for i, num in my_dict:
        # Calculate complement
        complement = target - num
        if complement in new_dict:
            # Return indices if complement is found
            return [new_dict[complement], i]
        # Store index of the current element
        new_dict[num] = i


# Example usage
nums, target = [2, 7, 11, 15], 26
print(twoSum(nums, target))
