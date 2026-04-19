from functools import cache
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        res = 1
        cache = {}
        def dfs(i, j):
            if (i, j) in cache:
                return cache[(i, j)]
            
            maxLen = 1
            for di, dj in ((1, 0), (0, 1), (-1, 0), (0, -1)):
                if (0 <= i + di < m and 0 <= j + dj < n) and matrix[i + di][j + dj] > matrix[i][j]:
                    cache[(i + di, j + dj)] = dfs(i + di, j + dj)
                    maxLen = max(maxLen, 1 + cache[(i + di, j + dj)])
            return maxLen
        
        return max(dfs(i, j) for i in range(m) for j in range(n))