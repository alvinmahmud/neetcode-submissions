class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxL = 0

        if len(s) == 1: return 1
        if len(s) == 0: return 0

        l, r = 0, 0
        seen = {}

        while r < len(s) and l <= r:
            seen[s[r]] = seen.get(s[r], 0) + 1

            while seen[s[r]] > 1:
                seen[s[l]] -= 1
                l += 1

            substring = s[l : r + 1]
            maxL = max(maxL, len(substring))
            r += 1
        return maxL
