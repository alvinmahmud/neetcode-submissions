class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        ans = []
        l, r = 0, k - 1

        while r < len(nums):
            curr = nums[l : r + 1]
            ans.append(max(curr))
            l += 1
            r += 1
        return ans