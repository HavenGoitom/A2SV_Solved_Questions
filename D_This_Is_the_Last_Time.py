t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    # print(k)
    casino = []

    for i in range(n):
        l, r, real = map(int, input().split())
        casino.append([l, r, real])

    casino.sort()
    k
    # print(casino)

    for i in range(len(casino)):
        if casino[i][0]<=k<=casino[i][1]:
            k = max(k,casino[i][2])
    print(k)
