n,s = map(int, input().split(" "))
a = list(map(int, input().split(" ")))

def big_sum(n,s,a):
    count = 0
    left = 0
    total = 0

    for right in range(n):

        total += a[right]
        
        while total >= s:
            count += n - right
            total -= a[left]
            left += 1

        

    return count


print(big_sum(n,s,a))
