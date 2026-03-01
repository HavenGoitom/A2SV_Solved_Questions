from collections import Counter

t = int(input())
for _ in range(t):
    n, l, r = map(int, input().split())
    socks = list(map(int, input().split()))

    left = Counter(socks[:l])
    right = Counter(socks[l:])

    for c in list(left.keys()):
        m = min(left[c], right[c])
        left[c] -= m
        right[c] -= m
        l -= m
        r -= m

    cost = 0

    
    if l < r:
        left, right = right, left
        l, r = r, l

    
    need = (l - r) // 2

    for c in left:
        if need == 0:
            break
        pairs = left[c] // 2
        take = min(pairs, need)

        left[c] -= take * 2
        l -= take * 2
        cost += take
        need -= take

    
    cost += (l - r) // 2

   
    cost += (l + r) // 2

    print(cost)