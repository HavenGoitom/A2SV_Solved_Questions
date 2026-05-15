class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        n = len(grid)
        parent = {(i, j, k): (i, j, k) for i in range(n) for j in range(n) for k in range(2)}
        size = {(i, j, k): 1 for i in range(n) for j in range(n) for k in range(2)}

        def find(x):
            while x != parent[x]:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x
        
        def union(x, y):
            x = find(x)
            y = find(y)
            if x != y:
                if size[x] < size[y]:
                    x, y = y, x
                size[x] += size[y]
                parent[y] = x
            
        for i in range(n):
            for j in range(n):
                if grid[i][j] == " ":
                    union((i, j, 0), (i, j, 1))
                    if i: union((i, j, 0), (i - 1, j, 1))
                    if j and grid[i][j - 1] != "\\": union((i, j, 0), (i, j - 1, 1))
                    elif j  and grid[i][j - 1] == "\\": union((i, j, 0), (i, j - 1, 0))
                elif grid[i][j] == "/":
                    if i: union((i, j, 0), (i - 1, j, 1))
                    if j and grid[i][j - 1] != "\\": union((i, j, 0), (i, j - 1, 1))
                    elif j  and grid[i][j - 1] == "\\": union((i, j, 0), (i, j - 1, 0))
                else:
                    if i: union((i, j, 0), (i - 1, j, 1))
                    if j and grid[i][j - 1] != "\\": union((i, j, 1), (i, j - 1, 1))
                    elif j  and grid[i][j - 1] == "\\": union((i, j, 1), (i, j - 1, 0))

        pars = set()
        for i in range(n):
            for j in range(n):
                for k in range(2):
                    pars.add(find((i, j, k)))

        return len(pars)