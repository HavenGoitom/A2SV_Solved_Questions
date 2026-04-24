def DFS(node):
        visited[node] = True

        for neigbh in val[node]:
            if not visited[neigbh]:  
                DFS(neigbh)
        
        res.append(node)

    for i in range(n):
        if not visited[i]:
            DFS(i)

    res.reverse()

    print(*[x + 1 for x in res])