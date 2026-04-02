class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set()
        for num in nums:
            s.add(num)
        
        out = 0

        for num in nums:
            cur_length = 1

            cur = num
            while (cur + 1) in s:
                cur_length += 1
                cur = cur + 1

            out = max(out, cur_length)
            
        return out