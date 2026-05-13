class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        count = n
        parent = {i:i for i in range(n)}

        def find(x):
            while x != parent[x]:
                x = parent[x]
            return x
        
        def union(x, y):
            rootx = find(x)
            rooty = find(y)
            if rootx != rooty:
                parent[rooty] = rootx
                return True
            return False
        
        for i in range(n):
            for j in range(i+1, n):
                if isConnected[i][j]:
                    if union(i, j):
                        count -= 1
                    
        return count

