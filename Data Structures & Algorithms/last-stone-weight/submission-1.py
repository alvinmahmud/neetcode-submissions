class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        s = []
        for stone in stones:
            s.append(-stone)

        heapq.heapify(s)

        while len(s) > 1:
            y, x = heapq.heappop(s), heapq.heappop(s)
            y = -y
            x = -x

            if x != y:
                smashed = -(y - x)
                heapq.heappush(s, smashed)
        
        return -s[0] if len(s) else 0

