class Solution:
    def trap(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        maxL, maxR = nums[l], nums[r]
        ans = 0

        while l < r:
            if maxL < maxR:
                l += 1
                maxL = max(maxL, nums[l])
                ans += maxL - nums[l]
            else:
                r -= 1
                maxR = max(maxR, nums[r])
                ans += maxR - nums[r]
        
        return ans