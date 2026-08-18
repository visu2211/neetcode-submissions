class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        """
        Inputs / Outputs
        Givens / Assumptions
        Constraints
        Example
        Code
        Edge Cases
        Complexities
        """
        #if rows are empty, need to remove them on the col operations
        spiralList = []
        while matrix:
            #each iteration has four phases
            #top row
            spiralList += matrix[0]
            if len(matrix) > 1:
                matrix = matrix[1:]
            else:
                break
            print(spiralList)
            print(matrix)

            #last col
            if matrix:
                for i in range(len(matrix)):
                    spiralList.append(matrix[i][-1])
                    matrix[i].pop()
                if matrix[0] == []:
                    break
            print(spiralList)
            print(matrix)
            

            #bottom row
            if matrix:
                spiralList += matrix[-1][::-1]
                matrix = matrix[:-1]
            print(spiralList)
            print(matrix)


            #first col
            if matrix:
                subList = []
                for i in range(len(matrix)):
                    subList.append(matrix[i][0])
                    matrix[i] = matrix[i][1:]
                spiralList += subList[::-1]
                if matrix[0] == []:
                    break
            print(spiralList)
            print(matrix)


        return spiralList