n,s = map(int, input().split(" "))
a = list(map(int, input().split(" ")))

def small_spread(n,s,a):
    count = 0
    left = 0
    total = 0

    for right in range(n):
        
        total += a[right]
        curr_max = max()
        curr_min = min()

        while curr_max - curr_min > s:
            total -= a[left]
            left += 1

        count += (right - left + 1)

    return count


print(small_spread(n,s,a))
