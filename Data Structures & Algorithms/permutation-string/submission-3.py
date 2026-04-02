class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        count = {}
        for c in s1:
            count[c] = count.get(c, 0) + 1
        
        need = len(count)
        for i in range(len(s2)):
            count2, curr = {}, 0
            for j in range(i, len(s2)):
                count2[s2[j]] = count2.get(s2[j], 0) + 1

                if count.get(s2[j], 0) < count2.get(s2[j], 0):
                    break
                if count.get(s2[j], 0) == count2.get(s2[j], 0):
                    curr += 1
                if curr == need:
                    return True
        return False