class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set()
        for num in nums:
            s.add(num)
        
        if len(nums) == 0: return 0
        if len(nums) == 1: return 1
        
        out = 0

        for num in nums:
            cur_length = 1

            cur = num
            while (cur + 1) in s:
                cur_length += 1
                out = max(out, cur_length)
                cur = cur + 1
                
            out = max(out, cur_length)
            
        return out