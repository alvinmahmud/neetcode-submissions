class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        sort = sorted(nums)
        i, j = 0, 1

        while j < len(sort):
            if sort[i] == sort[j]:
                return sort[i]
            i += 1
            j += 1
        return -1