class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        num_map = {}  # Stores num: index
        for i, num in enumerate(nums):
            complement = target - num
            if complement in num_map:
                return [num_map[complement], i]
            num_map[num] = i
        return [] # Should not reach here for valid inputs