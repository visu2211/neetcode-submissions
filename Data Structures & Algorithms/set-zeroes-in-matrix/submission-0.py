class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        zeroes = []
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    zeroes.append([i, j])

        def zero(i, j):
            #mark all values in row to zero
            for c in range(len(matrix[i])):
                matrix[i][c] = 0

            #mark all values in col to zero
            for r in range(len(matrix)):
                matrix[r][j] = 0

        for i, j in zeroes:
            zero(i, j)
    