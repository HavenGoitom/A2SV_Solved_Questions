def canBe():
    n,s = map(int, input().split(" "))
    arr = list(map(int, input().split(" ")))

    present = set(arr)
    
    x = 1
    while s > 0:
        if x not in present:
            s -= x
            arr.append(x)
        x += 1
    
    if s == 0 and len(arr) == max(arr):
        return "YES"
    else:
        return "NO"
    

t = int(input())
for _ in range(t):
    print(canBe())