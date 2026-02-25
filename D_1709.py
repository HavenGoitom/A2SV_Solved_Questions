t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int,input().split(" ")))
    b = list(map(int,input().split(" ")))

    swaps = []
    count = 0

    for i in range(n):
        for j in range(0, n-1-i):

            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1],a[j]
                swaps.append((1,j+1))
                count += 1

            if b[j] > b[j+1]:
                b[j], b[j+1] = b[j+1],b[j]
                swaps.append((2,j+1))
                count += 1

    for i in range(n):
        if a[i] > b[i]:
            a[i],b[i] = b[i],a[i]
            swaps.append((3,i+1))
            count += 1

    print(count)
    if swaps:
        for swap in swaps:
            print(*swap)
    
    




