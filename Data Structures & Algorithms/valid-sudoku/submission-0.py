class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #check horizontal lines
        for i in range(len(board)):
            temp = [j for j in board[i] if j.isalnum()]
            if len(set(temp)) != len(temp):
                return False
        #check vertical lines
        for i in range(len(board)):
            checked = []
            for j in range(len(board)):
                if board[j][i].isalnum():
                    checked.append(board[j][i])
            if len(set(checked)) != len(checked):
                return False
        #check boxes
        for i in range(0, len(board), 3):
            for j in range(0, len(board), 3):
                checked = []
                if board[i][j].isalnum():
                    checked.append(board[i][j])
                if board[i + 1][j].isalnum():
                    checked.append(board[i + 1][j])
                if board[i + 2][j].isalnum():
                    checked.append(board[i + 2][j])
                if board[i][j + 1].isalnum():
                    checked.append(board[i][j + 1])
                if board[i][j + 2].isalnum():
                    checked.append(board[i][j + 2])
                if board[i + 1][j + 1].isalnum():
                    checked.append(board[i + 1][j + 1])
                if board[i + 2][j + 2].isalnum():
                    checked.append(board[i + 2][j + 2])
                if board[i + 2][j + 1].isalnum():
                    checked.append(board[i + 2][j + 1])
                if board[i + 1][j + 2].isalnum():
                    checked.append(board[i + 1][j + 2])
                if len(set(checked)) != len(checked):
                    return False
        return True
    