class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}
        ans = []

        for s in strs:
            srt = ''.join(sorted(s))
            if srt not in res:
                res[srt] = []
            
            res[srt].append(s)
        
        for key, value in res.items():
            ans.append(value)
        
        return ans
        
