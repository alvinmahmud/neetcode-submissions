class Solution:
    def minWindow(self, s: str, t: str) -> str:
        ans = ""
        if len(s) < len(t): 
            return ans

        need = Counter(t)
        current = Counter()
        have, left = 0, 0
        minimum = float('inf')

        for right in range(len(s)):
            c = s[right]
            if c in need:
                current[c] += 1
                if current[c] == need[c]:
                    have += 1
            
            while have == len(need):
                minimum = min(minimum, (right - left + 1))
                ans = s[left : right + 1]

                ch = s[left]
                if ch in need:
                    if current[ch] == need[ch]:
                        have -=1
                    current[ch] -= 1
                left += 1

        return ans
        
        

        