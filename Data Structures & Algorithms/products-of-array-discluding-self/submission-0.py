class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = []
        for i in range(len(nums)):
            temp = 1
            for j in range(len(nums)):
                if i == j:
                    continue
                temp *= nums[j]
            
            ans.append(temp)
        return ans