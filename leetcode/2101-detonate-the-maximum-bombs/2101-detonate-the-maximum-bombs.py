class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        
        n = len(bombs)
        graph = [[] for i in range(n)]

        for i in range(n):
            x1, y1, r1 = bombs[i] 

            for j in range(i+1, n):
                x2, y2, r2 = bombs[j]

                if r1**2 >= abs(x2-x1)**2 + abs(y2-y1)**2 :
                    graph[i].append(j)
                if r2**2 >= abs(x2-x1)**2 + abs(y2-y1)**2:
                    graph[j].append(i)
        
        # print(graph) [[1, 2], [], [1, 3], [1, 2, 4], [2, 3]] for eg 3

        queue = deque()
        ans = 0

        for i in range(n):

            visited = [False for i in range(n)]
            queue.append(i)
            count = 1
            visited[i] = True

            while queue:
                nei = queue.popleft()
                
                for neig in graph[nei]:
                    if not visited[neig]:
                        queue.append(neig)
                        visited[neig] = True
                        count += 1
            ans = max(ans, count)
        
        return ans
                    