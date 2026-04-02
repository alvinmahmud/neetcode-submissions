class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}

        for index, num in enumerate(nums):
            d[num] = index

        for index, value in enumerate(nums):
            if (target - value) in d and d[target - value] != index:
                return [index, d[target - value]]