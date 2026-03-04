from collections import Counter
import random

t = int(input())


MASK = random.getrandbits(30)

for _ in range(t):
    n, k = map(int, input().split())
    cards = list(map(int, input().split()))


    cards_map = {}

    for x in cards:
        hx = x ^ MASK
        cards_map[hx] = cards_map.get(hx, 0) + 1

    
    arr = []
    for hx, freq in cards_map.items():
        real_value = hx ^ MASK
        arr.append((real_value, freq))

    arr.sort()


    l = 0
    current_sum = 0
    ans = 0

    for r in range(len(arr)):

        current_sum += arr[r][1]

        if r > 0 and arr[r][0] != arr[r-1][0] + 1:
            l = r
            current_sum = arr[r][1]

        while r - l + 1 > k:
            current_sum -= arr[l][1]
            l += 1

        if current_sum > ans:
            ans = current_sum

    print(ans)