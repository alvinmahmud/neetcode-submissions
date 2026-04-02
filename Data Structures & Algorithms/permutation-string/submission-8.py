class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        l = 0
        r = len(s1) - 1

        dict1 = {}

        for c in s1:
            dict1[c] = dict1.get(c, 0) + 1
        
        while r < len(s2):
            window = s2[l:r+1]
            dict2 = {}

            for c in window:
                dict2[c] = dict2.get(c, 0) + 1

            if dict1 == dict2: 
                return True
            
            l += 1
            r += 1
        
        return False
