class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        d = {}             
        flag = False

        for num in nums:
            if num in d:
                d[num] += 1
            else:
                d[num] = 1

        for key, value in d.items():
            if value > 1:
                flag = True
        
        return flag