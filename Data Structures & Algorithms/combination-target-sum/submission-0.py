class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def backtrack(i, sm, arr, target):
            if sm < target and i < len(nums):
                sm += nums[i]
                arr.append(nums[i])
                backtrack(i, sm, arr, target)

                sm -= nums[i]
                arr.pop()
                backtrack(i + 1, sm, arr, target)
            elif sm == target:
                res.append(arr.copy())
                return
        
        backtrack(0, 0, [], target)
        return res
            