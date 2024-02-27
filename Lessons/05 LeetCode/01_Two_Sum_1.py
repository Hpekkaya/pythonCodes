class Solution:
    def __init__(self, nums: list[int], target: int):
        self.nums = nums
        self.target = target

    def twoSum(self):
        prevMap = {}

        for i, n in enumerate(nums):
            diff = target - n
            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[n] = i
        return


nums = [2, 7, 18, 35]
target = 53

print((nums, target))
