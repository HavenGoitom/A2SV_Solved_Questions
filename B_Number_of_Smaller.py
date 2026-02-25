len_n, len_m = map(int, input().split(" "))
n = list(map(int, input().split(" ")))
m = list(map(int, input().split(" ")))

smaller_count = []
l = 0



for i in range(len_m):
    
    while l<len_n:
        if m[i] <= n[l]:
            break
        l += 1
    smaller_count.append(l)

print(*smaller_count)


