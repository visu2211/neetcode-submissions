class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        return None

    def pop(self) -> None:
        self.stack.pop()
        return None
        

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        arr = []
        while self.stack:
            arr.append(self.stack.pop())
        val = min(arr)
        for i in range(len(arr) - 1, -1, -1):
            self.stack.append(arr[i])
        return val
