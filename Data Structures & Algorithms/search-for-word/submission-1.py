class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        visited = set()

        if len(word) == 0:
            return True
        
        def backtrack(x, y, i):
            if i == len(word):
                return True

            if not(0 <= x < len(board)) or not(0 <= y < len(board[0])):
                return False
            
            if board[x][y] != word[i] or (x, y) in visited:
                return False
            
            visited.add((x, y))
            res = backtrack(x + 1, y, i + 1) or backtrack(x - 1, y, i + 1) or backtrack(x, y + 1, i + 1) or backtrack(x, y - 1, i + 1)
            visited.remove((x, y))
            return res

        for i in range(len(board)):
            for j in range(len(board[0])):
                if word[0] == board[i][j] and backtrack(i, j, 0):
                    return True
        
        return False

        
