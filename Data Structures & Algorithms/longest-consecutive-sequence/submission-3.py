class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        seen = set(nums)

        for num in nums:
            if (num - 1) not in seen:
                temp = 1
                while (num + temp) in seen:
                    temp += 1
                longest = max(temp, longest)
        return longest
