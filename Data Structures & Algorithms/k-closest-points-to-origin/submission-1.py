class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        res = []
        for i in range(len(points)):
            points[i] = ((points[i][0] ** 2) + (points[i][1] ** 2)) ** (0.5) , points[i]
        
        heapq.heapify(points)
        for _ in range(k):
            res.append(heapq.heappop(points)[1])
        
        return res