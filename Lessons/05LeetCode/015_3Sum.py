def three_sum(nums, target):
    nums.sort()
    result = []
    n = len(nums)

    for i in range(n - 2):
        left = i + 1
        right = n - 1

        while left < right:
            total = nums[i] + nums[left] + nums[right]

            if total == target:
                result.append([nums[i], nums[left], nums[right]])
                left += 1
                right -= 1
            elif total < target:
                left += 1
            else:
                right -= 1

    return result


nums = [-1, 0, 1, 2, -1, -4]
target = 0
result = three_sum(nums, target)
print("Unique triplets:", result)
