class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        cross = [(-1,0),(0,-1),(0,1),(1,0)]
        pac, atl = set(), set()

        def notInBound(row,col):
            if len(heights) <= row or row < 0 or len(heights[0]) <= col or col < 0:
                return True
            return False

        
        def dfs(row,col,visited, prevHeight):
            if notInBound(row,col) or ((row,col)) in visited or heights[row][col] < prevHeight:
                return
            visited.add((row,col))

            for r,c in cross:
                nr = row + r
                nc = col + c
                dfs(nr, nc, visited, heights[row][col])


        for c in range(len(heights[0])):
            dfs(0, c, pac, heights[0][c])
            dfs(len(heights)-1, c, atl, heights[len(heights)-1][c] )

        for r in range(len(heights)):
            dfs(r, 0, pac, heights[r][0] )
            dfs(r, len(heights[0])-1,atl, heights[r][len(heights[0])-1])
        
        res = []
        for r in range(len(heights)):
            for c in range(len(heights[0])):
                if (r,c) in pac and (r,c) in atl:
                    res.append([r,c])
        
        return res