n = [1,2,3]
m = [1,4,6]

def checkOrder(n,m):
    l,r = 0, 1
    while r < len(n):
        if n[l] > n[r]:
            return False
        l += 1
        r += 1
    return True

print(checkOrder(n))
    