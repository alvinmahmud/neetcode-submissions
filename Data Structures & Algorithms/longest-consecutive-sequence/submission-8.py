class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set()
        seen = set()

        for num in nums:
            s.add(num)
        
        out = 0

        for num in nums:
            if num in seen: continue

            cur_length = 1
            cur = num
            
            while (cur + 1) in s:
                cur_length += 1
                cur = cur + 1
                seen.add(cur)

            out = max(out, cur_length)
            
        return out