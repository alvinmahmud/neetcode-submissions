class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        res = float('inf')

        if len(nums) == 1:
            return nums[0]

        while l < r:
            res = min(res, nums[l], nums[r])
            mid = (l + r) // 2

            if nums[mid] > nums[l] and nums[mid] > nums[r]:
                l = mid + 1
            
            elif nums[mid] < nums[l] and nums[mid] < nums[r]:
                res = min(res, nums[mid])
                r = mid - 1
            
            else:
                l += 1
                mid += 1
        
        return res