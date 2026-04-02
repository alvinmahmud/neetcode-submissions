class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        part = []

        def dfs(i):
            if i >= len(s):
                res.append(part.copy())
                return
            
            for j in range(i, len(s)):
                substr = s[i : j + 1]
                if self.is_palindrome(substr):
                    part.append(substr)
                    dfs(j + 1)
                    part.pop()
        
        dfs(0)
        return res
    
    def is_palindrome(self, word):
        l, r = 0, len(word) - 1
        while l < r:
            if word[l] != word[r]:
                return False
            l += 1
            r -= 1
        return True