class Solution(object):
    def transpose(self, matrix):
        rows = len(matrix)
        cols = len(matrix[0])
        transposed = []
        for i in range(cols):
            new_row = []
            for j in range(rows):
                new_row.append(matrix[j][i])
            transposed.append(new_row)
        return transposed

