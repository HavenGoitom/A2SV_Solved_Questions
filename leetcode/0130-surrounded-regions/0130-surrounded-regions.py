class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        cross = [(-1,0),(0,-1),(0,1),(1,0)]
        rows, cols = len(board), len(board[0])

        visited = [[False for _ in range(cols)] for _ in range(rows)]

        def notInBound(row, col):
            return row < 0 or col < 0 or row >= rows or col >= cols

        def dfs(row, col):
            if notInBound(row, col) or board[row][col] != 'O' or visited[row][col]:
                return
            
            visited[row][col] = True

            for r, c in cross:
                dfs(row + r, col + c)

        for r in range(rows):
            for c in range(cols):
                if (r == 0 or c == 0 or r == rows - 1 or c == cols - 1) and board[r][c] == 'O':
                    dfs(r, c)

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 'O' and not visited[r][c]:
                    board[r][c] = 'X'