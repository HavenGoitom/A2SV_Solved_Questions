t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    b.sort()

    prev = -10**30
    ok = True

    for i in range(n):
        left = 0
        right = m - 1
        best = float('inf')

        if a[i] >= prev:
            best = a[i]

        while left <= right:
            mid = (left + right) // 2   
            val = b[mid] - a[i]

            if val >= prev:
                best = min(best, val)
                right = mid - 1
            else:
                left = mid + 1

        if best == float('inf'):
            ok = False
            break

        a[i] = best
        prev = best

    if ok:
        print("YES")
    else:
        print("NO")