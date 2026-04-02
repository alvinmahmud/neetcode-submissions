class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        count1 = {}
        for c in s1:
            count1[c] = count1.get(c, 0) + 1
        
        count2 = {}
        left = 0
        for i in range(len(s2)):
            count2[s2[i]] = count2.get(s2[i], 0) + 1
            if count1 == count2:
                return True
            
            if (i - left + 1) >= len(s1):
                count2[s2[left]] -= 1
                if count2[s2[left]] == 0:
                    del count2[s2[left]]
                left += 1

        return False