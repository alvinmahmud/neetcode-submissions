class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        res = []

        for num in nums:
            heapq.heappush(res, -num)

        while k > 1 and len(res):
            heapq.heappop(res)
            k -= 1
        
        return res[0] * -1