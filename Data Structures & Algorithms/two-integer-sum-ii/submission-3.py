class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        left, right = 0, len(nums) - 1

        while left < right:
            if nums[left] + nums[right] == target:
                return [left + 1, right + 1]
            
            elif nums[left] + nums[right] < target:
                left += 1
            
            else:
                right -= 1
            
        return [-1, -1]