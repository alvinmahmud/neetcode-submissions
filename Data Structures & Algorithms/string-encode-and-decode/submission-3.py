class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""

        for s in strs:
            encoded += str(len(s)) + "#" + s
        
        print(encoded)
        return encoded

    def decode(self, s: str) -> List[str]:
        decoded = []
        i = 0

        while i < len(s):
            length = 0
            while s[i] != "#":
                length = length * 10 + int(s[i])
                i += 1
            
            i += 1
            word = ""
            for _ in range(length):
                word += s[i]
                i += 1
            
            decoded.append(word)
            print(decoded)
        
        return decoded
                    