class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = set()
        
        for i in range(len(nums)):
            l, r = i + 1, len(nums) - 1
            while l < r:
                tmp = nums[i] + nums[l] + nums[r]
                if tmp < 0: 
                    l += 1
                elif tmp > 0: 
                    r-= 1
                else: 
                    ans.add((nums[i], nums[l], nums[r]))

                    while l < r and nums[l] == nums[l + 1]:
                        l += 1
                    while l < r and nums[r] == nums[r - 1]:
                        r -= 1
                    l += 1
                    r -=1
        
        return [list(triplet) for triplet in ans]