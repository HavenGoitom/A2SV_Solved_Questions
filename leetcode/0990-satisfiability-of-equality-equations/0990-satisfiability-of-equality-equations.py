class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        n = len(equations)
        parent = [i for i in range(26)]
        size = [1]*26

        def find(x):
            while x != parent[x]:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x
        
        def union(x,y):
            px = find(x)
            py = find(y)
            
            if px == py:
                return False
            
            if size[px] > size[py]:
                parent[py] = px
                size[px] += size[py]
            else:
                parent[px] = py
                size[py] += size[px]
            
            return True
        
        for i in range(n):
            x = ord(equations[i][0])-97
            y = ord(equations[i][3])-97

            if equations[i][1] == '=':
                union(x,y)

        for i in range(n):
            x = ord(equations[i][0])-97
            y = ord(equations[i][3])-97

            if equations[i][1] == '!':
                p1 = find(x)
                p2 = find(y)
                ans = (p1 == p2)
                if ans:
                    return False
        return True

            