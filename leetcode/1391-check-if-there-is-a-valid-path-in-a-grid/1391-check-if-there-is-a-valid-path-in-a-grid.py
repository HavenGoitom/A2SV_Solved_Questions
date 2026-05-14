class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        size = 6
        n = len(grid)
        m = len(grid[0])

        move = {
            1: [(0, -1), (0, 1)],
            2: [(-1, 0), (1, 0)],
            3: [(0, -1), (1, 0)],
            4: [(0, 1), (1, 0)],
            5: [(0, -1), (-1, 0)],
            6: [(0, 1), (-1, 0)],
        }

        parent = [i for i in range(n*m)]


        def inBound(x , y):
            if 0 <= x < len(grid) and 0 <= y < len(grid[0]):
                return True
            return False

        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x
        
        def union(x, y):
            parentx = find(x)
            parenty = find(y)

            if parentx != parenty:
                parent[parenty] = parentx
            
            
        for i in range(n):
            for j in range(m):

               for d in move[grid[i][j]]:
                    u = i + d[0] 
                    v = j + d[1]

                    if not inBound(u, v):
                        continue
                    
                    a = i*m+j
                    b = u*m+v

                    d3, d4 = move[grid[u][v]]

                    if inBound(u + d3[0], v + d3[1]):
                        if u + d3[0] == i and v + d3[1] == j:
                            union(a, b)

                    if inBound(u + d4[0], v + d4[1]):
                        if u + d4[0] == i and v + d4[1] == j:
                            union(a, b)
        a = 0
        b = n*m - 1 
        print(parent)
    
        return find(a) == find(b)
