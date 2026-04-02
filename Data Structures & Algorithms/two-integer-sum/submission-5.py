class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dictionary = {}

        for idx, num in enumerate(nums):
            dictionary[num] = idx
        
        for i in range(len(nums)):
            diff = target - nums[i] # this is what we look for in the dict

            if diff in dictionary and i != dictionary[diff]:
                return [i, dictionary[diff]]
            
        return []
