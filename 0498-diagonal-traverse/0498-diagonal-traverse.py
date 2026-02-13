class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        m = len(mat)
        n = len(mat[0])

        diagonal = [[] for _ in range(m + n - 1)]

        # print(diagonal)
        for i in range(m):
            for j in range(n):
                diagonal[i+j].append(mat[i][j])

        # print(diagonal)

        for i in range(len(diagonal)):
            if i % 2 == 0:
                diagonal[i].reverse()
        
        # print(diagonal)
        diagonal_ans = [num for nums in diagonal for num in nums]

        return diagonal_ans