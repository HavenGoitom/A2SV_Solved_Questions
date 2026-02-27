n,s = map(int, input().split(" "))
a = list(map(int, input().split(" ")))

def small_sum(n,s,a):
    count = 0
    left = 0
    total = 0

    for right in range(n):
        
        total += a[right]

        while total > s:
            total -= a[left]
            left += 1

        count += (right - left + 1)

    return count


print(small_sum(n,s,a))
