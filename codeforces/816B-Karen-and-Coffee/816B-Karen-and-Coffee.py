import sys

n, k, q = map(int, input().split())

intervals = []
queries = []
coords = set()

for _ in range(n):
    l, r = map(int, input().split())
    intervals.append((l, r))
    coords.add(l)
    coords.add(r + 1)

for _ in range(q):
    a, b = map(int, input().split())
    queries.append((a, b))
    coords.add(a)
    coords.add(b + 1)

coords = sorted(coords)
idx = {v: i for i, v in enumerate(coords)}

m = len(coords)

diff = [0] * (m + 1)

for l, r in intervals:
    diff[idx[l]] += 1
    diff[idx[r + 1]] -= 1

cover = 0
good_prefix = [0] * (m + 1)

for i in range(m - 1):
    cover += diff[i]

    length = coords[i + 1] - coords[i]

    if cover >= k:
        good_prefix[i + 1] = good_prefix[i] + length
    else:
        good_prefix[i + 1] = good_prefix[i]

for a, b in queries:
    l = idx[a]
    r = idx[b + 1]
    print(good_prefix[r] - good_prefix[l])