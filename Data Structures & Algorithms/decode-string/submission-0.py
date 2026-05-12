class Solution:
    def decodeString(self, s: str) -> str:
        self.i = 0

        def rec():
            res = ""
            k = 0

            while self.i < len(s):
                char = s[self.i]

                if char.isdigit():
                    self.i += 1
                    k = k * 10 + int(char)
                elif char == '[':
                    self.i += 1
                    inner = rec()
                    res += k * inner
                    k = 0
                elif char == ']':
                    self.i += 1
                    return res
                else:
                    self.i += 1
                    res += char
            return res
        return rec()