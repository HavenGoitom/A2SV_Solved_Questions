t = int(input())

for _ in range(t):
    n,k = map(int, input().split(" "))
    s = input()

    min_repaint = n
    window = 0
    white_count = 0
    left = 0

    for i in range(n):

        if s[i] == "W":
            white_count += 1

        window += 1

        if window > k:
            if s[left] == "W":
                white_count -= 1
            window -= 1
            left += 1

        if window == k:
            min_repaint = min(min_repaint, white_count)

    
    print(min_repaint)
