class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        target  = len(graph) - 1
        res = []

        def dfs(node, arr):

            nonlocal res

            arr.append(node)

            if node == target:
                res.append(arr.copy())
            else:
                for nd in graph[node]:
                    dfs(nd, arr)

            arr.pop()
        
        dfs(0, [])

        return res