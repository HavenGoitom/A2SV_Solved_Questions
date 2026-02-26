n,s = map(int, input().split(" "))
a = list(map(int, input().split(" ")))

def segement(n,s,a):
    left = 0
    right = 0
    total = a[left]
    res = n

    for right in range(n):

        while total < s and left<n:
            left += 1
            total += a[left]

        res = min(n, right - left + 1)
        total -= a[right]

    return res
        

    

print(segement(n,s,a))
        
        