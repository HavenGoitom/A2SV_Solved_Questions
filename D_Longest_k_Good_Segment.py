n,k = map(int, input().split(" "))
a = list(map(int, input().split(" ")))

unique = {}
left = 0
max_len = 0
res = []

for right in range(n):
    
    while len(unique) > k:
        unique[a[left]] -= 1

        if unique[a[left]] == 0:
            del unique[a[left]]

        left += 1

    if a[right] not in unique:
        unique[a[right]] = 1
    else:       
        unique[a[right]] += 1

    if len(unique) <= k:
        if max_len < (right - left + 1):
            max_len = right - left + 1
            res = [left + 1, right +1]


print(*res)
