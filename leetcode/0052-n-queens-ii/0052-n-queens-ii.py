class Solution:
    def totalNQueens(self, n: int) -> int:
        col = set()
        negDiag = set()
        postDiag = set()
        count = 0

        board = [["."] * n for i in range(n)]
        def backtracking(r):
            nonlocal count
            if r == n:
                count += 1
                return
            
            for c in range(n):
                if c in col or (r - c) in negDiag  or (r + c) in postDiag:
                    continue
                
                col.add(c)
                negDiag.add(r - c)
                postDiag.add(r + c)
                board[r][c] = "Q"

                backtracking(r + 1)

                col.remove(c)
                negDiag.remove(r - c)
                postDiag.remove(r + c)
                board[r][c] = "."

        backtracking(0)
        return count