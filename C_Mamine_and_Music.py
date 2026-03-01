from collections import defaultdict
n,k = map(int, input().split())
a = list(map(int, input().split(" ")))

hash_map = defaultdict(int)

for i in range(n):
    if hash_map[a[i]] == 0:
        hash_map[a[i]] = []
    hash_map[a[i]].append(i+1)

# print(hash_map)

a.sort()
vals = []

for i in range(n):
    if a[i] > k:
        break
    k -= a[i]
    vals.append(a[i])

# print(vals)
res = []

for val in vals:
    res.append(hash_map[val][-1])
    c = hash_map[val].pop()
    # print(c)

print(len(res))
print(*res)

    






