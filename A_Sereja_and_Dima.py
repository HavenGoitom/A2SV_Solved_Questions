n = int(input())
cards = list(map(int, input().split(" ")))

left,right = 0, n-1
players = [0,0] #Sereja and Dima
i = 0
while left <= right:

    # print(cards[right], cards[left])

    if cards[right] > cards[left]:
        players[i] += cards[right]
        # print(players[i])
        right -= 1
        if i == 0:
            i = 1
        else:
            i = 0
    else:
        players[i] += cards[left]
        # print(players[i])
        left += 1
        if i == 0:
            i = 1
        else:
            i = 0

print(*players)
