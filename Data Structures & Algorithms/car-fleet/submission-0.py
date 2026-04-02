class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = [] 
        sort = sorted(zip(position, speed), reverse = True)

        for pos, speed in sort:
            time = (target - pos) / speed
            stack.append(time)

            if len(stack) >= 2 and time <= stack[-2]:
                stack.pop()

        return len(stack)
