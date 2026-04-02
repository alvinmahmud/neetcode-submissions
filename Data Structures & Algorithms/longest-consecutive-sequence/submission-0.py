class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        seen = set(nums)

        for num in nums:
            count, current = 0, num
            while (current in seen):
                count += 1
                current += 1
            longest = max(longest, count)
        return longest
