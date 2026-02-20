n = int(input())

idxs = []
res = None

for i in range(n):
    a, b = map(int, input().split())
    idxs.append((a, b, i))  

idxs.sort(key=lambda x: (x[0], -x[1]))

for i in range(n-1):

    if idxs[i+1][1] <= idxs[i][1]:
        res = (idxs[i+1][2]+1, idxs[i][2]+1)  
        break

if res:
    print(res[0], res[1])
else:
    print(-1, -1)
