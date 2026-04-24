class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        color = [-1 for i in range(n)]

        def dfs(node):

            for nb in graph[node]:
                if color[nb] == -1:
                    color[nb] = 1 - color[node]
                    if not dfs(nb):
                        return False
                else:
                    if color[nb] == color[node]:
                        return False
            return True
        
        for node in range(n):
            if color[node] == -1:
                color[node] = 0
                if not dfs(node):
                    return False
        return True