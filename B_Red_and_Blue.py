t = int(input())

for _ in range(t):
    n = int(input())
    r = list(map(int, input().split(" ")))
    m = int(input())
    b = list(map(int, input().split(" ")))

    total1 = 0
    for i in range(n):
        total1 += r[i]
        r[i] = total1


    total2 = 0

    for i in range(m):
        total2 += b[i]
        b[i] = total2

    max_val_r = max(0, max(r))
    max_val_b = max(0, max(b))

    
    print(max_val_b + max_val_r)
    