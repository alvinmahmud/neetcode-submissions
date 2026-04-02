class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low, high = 0, len(nums) - 1

        while low <= high:
            mid = (low + high) // 2
            cur = nums[mid]

            if cur > target:
                high = mid - 1
            elif cur < target:
                low = mid + 1
            else:
                return mid
        return -1