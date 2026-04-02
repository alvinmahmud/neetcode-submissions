class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = math.ceil(sum(piles) / h)
        right = max(piles)
        ans = right

        while left <= right:
            mid = (left + right) // 2
            time = 0

            for i in piles:
                time += math.ceil(i / mid)
                if time > h:
                    break
            
            if time <= h:
                ans = min(ans, mid)
                right = mid - 1
            else:
                left = mid + 1
        
        return ans