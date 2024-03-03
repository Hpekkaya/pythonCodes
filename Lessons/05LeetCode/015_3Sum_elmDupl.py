def three_sum(nums, target):
    nums.sort()
    n = len(nums)
    triplets = []

    for i in range(n - 2):
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        left, right = i + 1, n - 1

        while left < right:
            total = nums[i] + nums[left] + nums[right]

            if total == target:
                triplets.append([nums[i], nums[left], nums[right]])
                left += 1
                right -= 1

                while left < right and nums[left] == nums[left - 1]:
                    left += 1
                while left < right and nums[right] == nums[right + 1]:
                    right -= 1

            elif total < target:
                left += 1
            else:
                right -= 1

    return triplets


nums = [-1, 0, 1, 2, -1, -4]
target = 0
result = three_sum(nums, target)
print("Unique triplets:", result)
