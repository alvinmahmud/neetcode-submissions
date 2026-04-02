class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {")": "(", "}": "{", "]": "[" }
        stack = []

        removed = 0

        if len(s) <= 1 or len(s) % 2 != 0:
            return False

        for c in s:
            if c in brackets:
                removed += 1
                if stack and stack[-1] == brackets[c]:
                    removed -= 1
                    stack.pop()
            
            else:
                stack.append(c)

        return not stack and not removed
