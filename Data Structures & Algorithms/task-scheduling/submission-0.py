class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = {}
        for c in tasks:
            count[c] = 1 + count.get(c, 0)
        time = 0
        q = deque()

        count = [-c for c in count.values()]
        heapq.heapify(count)

        while count or q:
            
            if count:
                task = heapq.heappop(count) + 1

                if task and task < 0:
                    q.append((task, time + n))

            if q and time >= q[0][1]:
                x = q.popleft()
                heapq.heappush(count, x[0])

            time += 1

        return time
