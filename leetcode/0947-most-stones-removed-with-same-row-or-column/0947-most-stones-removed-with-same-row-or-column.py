class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        n = len(stones)
        parent = [i for i in range(n)]
        size = [1]*n

        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        def union(x,y):
            px = find(x)
            py = find(y)

            if px == py:
                return
            
            if size[px] > size[py]:
                parent[py] = px
                size[px] += size[py]
            else:
                parent[px] = py
                size[py] += size[px]
        
        for i in range(n):
            for j in range(i + 1, n):
                if stones[i][0] == stones[j][0] or stones[i][1] == stones[j][1]:
                    union(i,j)

        seen = set()
        for i in range(n):
            seen.add(find(i))

        components = len(seen)

        return n - components