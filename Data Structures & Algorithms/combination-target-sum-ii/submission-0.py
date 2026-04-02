class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        def backtrack(i, curr, arr):
            seen = set()

            if curr == target:
                res.append(arr.copy())
                return
            
            if i >= len(candidates) or curr > target:
                return

            for j in range(i, len(candidates)):
                if candidates[j] in seen:
                    continue
                
                arr.append(candidates[j])
                seen.add(candidates[j])
                backtrack(j + 1, curr + candidates[j], arr)
                arr.pop()

        backtrack(0, 0, [])
        return res
