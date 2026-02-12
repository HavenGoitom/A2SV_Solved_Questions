class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        for i in range(len(matrix)):
            for j in range(i,len(matrix[0])):
                matrix[j][i],matrix[i][j] = matrix[i][j], matrix[j][i]


        print(matrix)


        for i in range(len(matrix)):
            l,r=0,len(matrix[0])-1
            while l < r:
                matrix[i][l], matrix[i][r] = matrix[i][r],matrix[i][l]
                l += 1
                r -= 1

            
        print(matrix)
