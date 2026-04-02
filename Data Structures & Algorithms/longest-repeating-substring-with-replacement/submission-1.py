class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        ans = 0
        chars = set(s)

        for c in chars:
            currCount = 0
            l = 0

            for r in range(len(s)):
                if s[r] == c:
                    currCount += 1
                
                while (r - l + 1) - currCount > k:
                    if s[l] == c:
                        currCount -= 1
                    l += 1
                
                ans = max(ans, r - l + 1)
        return ans
            