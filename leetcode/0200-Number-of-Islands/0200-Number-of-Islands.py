class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        cross = [(-1,0),(0,-1),(0,1),(1,0)]
        count = 0
        
        def notInBound(row,col):
            if len(grid) <= row or row < 0 or len(grid[0]) <= col or col < 0:
                return True

        def dfs(graph, row, col):
            if notInBound(row,col) or graph[row][col] == '0':
                return 

            graph[row][col] = '0'

            for r,c in cross:
                nr = r + row
                nc = c + col

                if not notInBound(nr, nc):
                    dfs(graph, nr, nc)
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    count += 1
                dfs(grid, i, j)
                    
        
        return count