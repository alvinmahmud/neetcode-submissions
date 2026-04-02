class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        def backtrack(i, curr, arr):
            if curr == target:
                res.append(arr.copy())
                return
            
            if i >= len(candidates) or curr > target:
                return

            for j in range(i, len(candidates)):
                if j > i and candidates[j] == candidates[j - 1]:
                    continue
                
                arr.append(candidates[j])
                backtrack(j + 1, curr + candidates[j], arr)
                arr.pop()

        backtrack(0, 0, [])
        return res
