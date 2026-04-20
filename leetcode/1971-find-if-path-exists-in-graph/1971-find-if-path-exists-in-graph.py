class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        
        # hashmap = defaultdict(list)
        graph = [[] for _ in range(n)]
        visited = [False for _ in range(n)]

        for p,n in edges:
            graph[p].append(n)
            graph[n].append(p)
        
        # print(graph)

        found = False
        ans  = False

        def helper(node, visited):
            nonlocal found
            nonlocal ans
            if node == destination:
                ans = ans or True
                return ans

            visited[node] = True

            for n in graph[node]:
                if not visited[n]:
                    helper(n, visited)
                # if found:
                #     return True
            # return False

        helper(source, visited)   
        return ans
         
