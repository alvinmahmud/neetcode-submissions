class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for c in tokens:
            if c not in '+-*/':
                stack.append(int(c))
            else:
                n2, n1 = stack.pop(), stack.pop()
                if c == '+':
                    res = n1 + n2
                elif c == '-':
                    res = n1 - n2
                elif c == '*':
                    res = n1 * n2
                elif c == '/':
                    res = n1 / n2
                stack.append(int(res))
        return stack[-1]