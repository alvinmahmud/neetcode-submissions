class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        letters = {
            2: ["a", "b", "c"],
            3: ["d", "e", "f"],
            4: ["g", "h", "i"],
            5: ["j", "k", "l"],
            6: ["m", "n", "o"],
            7: ["p", "q", "r", 's'],
            8: ["t", "u", "v"],
            9: ["w", "x", "y", "z"]
        }

        res = []

        if not digits:
            return res

        def dfs(i, s):
            if i == len(digits) or len(s) == len(digits):
                res.append(s)
                return
            
            arr = letters[int(digits[i])]
            for char in arr:
                s += char
                dfs(i + 1, s)
                s = s[:-1]
        
        dfs(0, "")
        return res