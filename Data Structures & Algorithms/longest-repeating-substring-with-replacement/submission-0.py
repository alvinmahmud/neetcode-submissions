class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        ans = 0

        for i in range(len(s)):
            counts = [0] * 26
            currMax = 0

            for j in range(i, len(s)):
                counts[ord(s[j]) - ord('A')] += 1
                currMax = max(currMax, counts[ord(s[j]) - ord('A')])

                if (j - i + 1) - currMax <= k:
                    ans = max(ans, (j - i + 1))
        
        return ans
            