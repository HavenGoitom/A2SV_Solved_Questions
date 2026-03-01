from collections import Counter

t = int(input())

# sliding window sort the hash_map kedemesh if you're going to use that to avoid colloison we can also xor it to avoid the collision.

for _ in range(t):
    n,k = map(int, input().split())
    cards = list(map(int, input().split()))

    cards_map = Counter(cards)

    values = list(cards_map.values())

    values.sort()
    cards.sort()

    cards = set(cards)
    #print(cards) {2, 3, 4, 5}

    # print(values) [2, 2, 3, 3]

    k_stop = 0
    count = 0

    for num in cards:
        cards_map[num] == values[-1]
        count += values[-1]
        k_stop += 1
        values.pop()

        if k_stop == k:
            break


    print(count)