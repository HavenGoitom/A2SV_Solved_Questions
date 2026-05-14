class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges) + 1
        parent = [i for i in range(n)]
        size = [1]*n

        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x
        
        def union(x,y):
            parentx = find(x)
            parenty = find(y)

            if parentx == parenty:
                return False
            
            if size[parentx] > size[parenty]:
                parent[parenty] = parentx
                size[parentx] += size[parenty]
            else:
                parent[parentx] = parenty
                size[parenty] += size[parenty]
            return True

            
        for x,y in edges:
            if not union(x,y):
                return x,y


        
