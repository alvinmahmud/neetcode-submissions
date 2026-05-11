class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        cnt = Counter(tasks)
        h = [-c for c in cnt.values()]
        heapq.heapify(h)

        time = 0
        q = deque()

        while h or q:
            time += 1

            if h:
                c = heapq.heappop(h) + 1 # remove a task
                if c != 0:
                    q.append([c, time + n]) # queue holds new count and next time avail.
            
            if q and q[0][1] == time:
                new = q.popleft()
                heapq.heappush(h, new[0])
        
        return time
            