class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        ans, l, curr = 0, 0, 0

        for r in range(len(s)):
            count[s[r]] = count.get(s[r], 0) + 1
            curr = max(curr, count[s[r]])

            while (r - l + 1) - curr > k:
                count[s[l]] -= 1
                l += 1
            
            ans = max(ans, r -l + 1)
        return ans
            