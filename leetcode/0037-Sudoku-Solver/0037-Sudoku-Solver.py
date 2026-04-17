class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        normal = defaultdict(set)

        for row in range(9):
            for col in range(9):
                if board[row][col] != ".":
                    normal[(-1, row)].add(int(board[row][col]))
                    normal[(-2, col)].add(int(board[row][col]))
                    normal[((row // 3) *3,(col // 3) *3)].add(int(board[row][col]))                
            
        def helper(row, col):
            if row == 9:
                return True

            if col + 1 != 9:
                new_row, new_col = row, col + 1
            else:
                new_row, new_col = row + 1, 0

            if board[row][col] != '.':
                return helper(new_row, new_col)
            
            for opt in range(1,10):
                if opt in normal[(-1,row)] or opt in normal[(-2, col)] or opt in normal[((row // 3) *3,(col // 3) *3)]:
                    continue
                
                normal[(-1, row)].add(opt)
                normal[(-2, col)].add(opt)
                normal[((row // 3) *3, (col // 3) *3)].add(opt)     
                board[row][col] = str(opt)

                if helper(new_row, new_col):
                    return True
                
                normal[(-1, row)].remove(opt)
                normal[(-2, col)].remove(opt)
                normal[((row // 3) *3,(col // 3) *3)].remove(opt)  
                board[row][col] = '.'


            return False
        
        helper(0,0)