n,s = map(int, input().split(" "))
a = list(map(int, input().split(" ")))

def segement(n,s,a):
    total = sum(a)
    n -= 1
    if total <= s:
        return n
    
    left = 0
    right = n

    while left < right:
        if a[left]>a[right]:
            total -= a[left]
            n -= 1
        else:
            total -= a[right]
            n -= 1
        if total <= s:
            return n
    return 0

print(segement(n,s,a))
        
        