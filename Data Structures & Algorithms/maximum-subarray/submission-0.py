class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = float('-inf')
        r = 0

        if len(nums) == 1: return nums[0]

        curSum = 0
        while r < len(nums):
            if curSum < 0:
                curSum = 0
            
            curSum += nums[r]
            r += 1
            maxSum = max(maxSum, curSum)
        
        return maxSum
