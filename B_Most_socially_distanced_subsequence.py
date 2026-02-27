t = int(input())

for i in range(t):
    n = int(input())
    p = list(map(int, input().split(" ")))

    res = []

    for i in range(n):
        res.append(p[i])

        if len(res) > 2:

            if res[-3]>res[-2]>res[-1] or res[-3]<res[-2]<res[-1]:
                end = res.pop()
                res.pop()
                res.append(end)

    print(len(res))
    print(*res)