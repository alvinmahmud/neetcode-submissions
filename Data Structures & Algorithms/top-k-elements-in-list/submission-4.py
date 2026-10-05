class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c = {}
        for num in nums:
            if num in c:
                c[num] += 1
            else:
                c[num] = 0
        
        heap = []
        for num, count in c.items():
            heapq.heappush(heap, (count, num))

            if len(heap) > k:
                heapq.heappop(heap)
        
        res = []
        for count, num in heap:
            res.append(num)
        
        return res