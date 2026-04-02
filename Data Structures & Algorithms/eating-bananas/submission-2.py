class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # min eating speed and max speeding speed (min can't be 0)
        l, r = 1, max(piles)

        # set initial answer to max and go down if needed
        res = r

        # run binary search from the middle and go up/down depending on if we need to be slower or faster

        while l <= r:
            # mid way point
            k = (l + r) // 2

            time = 0

            for p in piles:
                time += math.ceil(float(p) / k)
            
            if time <= h:
                # after we have seen all the piles and we are still under the hours (valid)
                res = k

                # set right pointer to see if we can do better
                r = k - 1
            else:
                # can't do lower so we set left pointer
                l = k + 1
        
        return res

