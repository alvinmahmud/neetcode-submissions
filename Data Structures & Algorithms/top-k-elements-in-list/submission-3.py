class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c = Counter(nums)
        res = []
        
        for num, count in c.items():
            heapq.heappush(res, (count, num))

            if len(res) > k:
                heapq.heappop(res)
            
        return [val for key, val in res]