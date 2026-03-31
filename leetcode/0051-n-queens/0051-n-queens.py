class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        postive_diagonal = set() #r+c
        negative_diagonal = set() #r-c
        curr_col = set()
        res = []
        board = [["."] * n for i in range(n)]
        # print(board) ['.', '.', '.', '.']
        def helper(r):
            if r == n:
                copy = ["".join(row) for row in board]
                res.append(copy)
                return
            
            for c in range(n):
                if c in curr_col or (r-c) in negative_diagonal or (r+c) in postive_diagonal:
                    continue

                postive_diagonal.add(r + c) 
                negative_diagonal.add(r - c)
                curr_col.add(c)
                board[r][c] = "Q"

                helper(r + 1)

                postive_diagonal.remove(r + c) 
                negative_diagonal.remove(r - c)
                curr_col.remove(c)
                board[r][c] = "."

        helper(0)
        return res