class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxL = 0

        if len(s) == 1: return 1
        if len(s) == 0: return 0

        l, r = 0, 0
        seen = set()

        while r < len(s) and l <= r:
            while s[r] in seen:
                seen.remove(s[l])
                l += 1

            seen.add(s[r])
            substring = s[l : r + 1]
            maxL = max(maxL, len(substring))

            r += 1
        return maxL
