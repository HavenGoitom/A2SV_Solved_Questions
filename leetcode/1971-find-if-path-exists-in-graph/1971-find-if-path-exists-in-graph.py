class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        
        # hashmap = defaultdict(list)
        graph = [[] for _ in range(n)]

        for p,n in edges:
            graph[p].append(n)
            graph[n].append(p)
        
        # print(graph)

        found = False

        def helper(node, visited):
            nonlocal found
            if node == destination:
                return True

            visited.add(node)

            for n in graph[node]:
                if n not in visited:
                    found = helper(n, visited)
                if found:
                    return True
            return False

        return helper(source, set())   
         
