class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []

        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][1]:
                temp = stack.pop()
                res[temp[0]] = i - temp[0]
            stack.append([i, t])
        return res