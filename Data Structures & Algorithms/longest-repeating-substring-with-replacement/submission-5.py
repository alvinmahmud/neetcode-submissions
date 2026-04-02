class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        longest = 0
        l, r = 0, 0

        maxF = 0
        cnt = {}

        while l <= r and r < len(s):
            cnt[s[r]] = cnt.get(s[r], 0) + 1
            maxF = max(maxF, cnt[s[r]])

            while (r - l + 1) - maxF > k:
                cnt[s[l]] -= 1
                l += 1

            longest = max(longest, (r - l + 1))
            r += 1

        return longest