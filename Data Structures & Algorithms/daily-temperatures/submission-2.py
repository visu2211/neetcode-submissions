class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []
        for i, t in enumerate(temperatures):
            if len(stack) == 0:
                stack.append((t, i))
            else:
                while len(stack) > 0 and t > stack[-1][0]:
                    ot, oi = stack[-1]
                    res[oi] = i - oi
                    stack.pop()
                stack.append((t, i))
        return res