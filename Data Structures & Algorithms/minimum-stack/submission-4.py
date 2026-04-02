class MinStack:

    def __init__(self):
        self.stack = []
        self.s2 = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        current = self.stack[-1]
        if len(self.s2):
            self.s2.append(min(self.s2[-1], current))
        else:
            self.s2.append(current)

    def pop(self) -> None:
        self.stack.pop()
        self.s2.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.s2[-1]
