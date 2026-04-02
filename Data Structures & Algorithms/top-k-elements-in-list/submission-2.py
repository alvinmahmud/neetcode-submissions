class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        bucket = {}
        count = {}
        out = []

        for i in range(len(nums)):
            bucket[len(nums) - i] = []

        for num in nums:
            if num not in count:
                count[num] = 1
            else:
                count[num] += 1

        for num, cnt in count.items():
            bucket[cnt].append(num)

        for count, values in bucket.items():
            for value in values:
                if len(out) == k:
                    break
                    
                out.append(value)

        return out
        
