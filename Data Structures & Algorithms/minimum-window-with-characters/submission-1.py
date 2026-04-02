class Solution:
    def minWindow(self, s: str, t: str) -> str:
        ans = ""
        if len(t) > len(s): return ans

        have, need = {}, {}
        for c in t:
            need[c] = need.get(c, 0) + 1
        
        mini = float('inf')
        left = 0
        matches = 0

        for right in range(len(s)):
            c = s[right]
            have[c] = have.get(c, 0) + 1

            if c in need and have[c] == need[c]:
                matches += 1
            
            while matches == len(need):
                if (right - left + 1) < mini:
                    ans = s[left : right + 1]
                    mini = (right - left) + 1

                ch = s[left]
                if ch in need:
                    if have[ch] == need[ch]:
                        matches -=1
                    have[ch] -= 1
                left += 1
            
        return ans if mini != float('inf') else ""

