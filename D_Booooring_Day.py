t = int(input())

for _ in range(t):
    n, l, r = map(int, input().split(" "))
    cards = list(map(int, input().split(" ")))

    count = 0
    left = 0
    total = 0

    for right in range(n):

        total += cards[right]

        while total > r and left <= right:
            total -= cards[left]
            left += 1
        
        if total >= l:
            count += 1
            total = 0
            left = right + 1

    print(count)

