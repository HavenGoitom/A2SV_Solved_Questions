class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        adj = [[] for _ in range(n)]
        indgree = [0 for _ in range(n)]
        queue = deque()
        parent = defaultdict(set)
        res = []

        for u,v in edges:
            adj[u].append(v)
            indgree[v] += 1
        
        for i in range(n):
            if indgree[i] == 0:
                queue.append(i)
        
        while queue:
            node = queue.pop()

            for nei in adj[node]:
                indgree[nei] -= 1

                parent[nei].add(node)
                parent[nei] = parent[nei].union(parent[node])

                if indgree[nei] == 0:
                    queue.append(nei)
        
        for i in range(n):
            arr = list(parent[i])
            arr.sort()
            res.append(arr)
            
        return res