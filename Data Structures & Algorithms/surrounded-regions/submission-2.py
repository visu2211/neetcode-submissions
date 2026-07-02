class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        find all border O's and run dfs on them and change them to T's.
        then turn all the other cells to Xs because those Os dont touch borders
        then flip the Ts
        """
        rows, cols = len(board), len(board[0])
        def dfs(x, y):
            if not(0 <= x < rows and 0 <= y < cols) or board[x][y] != "O":
                return
            
            board[x][y] = "T"
            dfs(x + 1, y)
            dfs(x, y + 1)
            dfs(x - 1, y)
            dfs(x, y - 1)

        for i in range(rows):
            if board[i][0] == "O":
                dfs(i, 0)
            if board[i][cols - 1] == "O":
                dfs(i, cols - 1)

        for j in range(cols):
            if board[0][j] == "O":
                dfs(0, j)
            if board[rows - 1][j] == "O":
                dfs(rows - 1, j)

        for i in range(rows):
            for j in range(cols):
                if board[i][j] == "O":
                    board[i][j] = "X"
                elif board[i][j] == "T":
                    board[i][j] = "O"