class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        """
        use a monotonic stack to get the max temperatures
        """
        stack = []
        res = [0] * len(temperatures)
        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                index = stack.pop()[1]
                res[index] = i - index
            stack.append((t, i))

        return res