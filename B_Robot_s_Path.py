n,k = map(int, input().split(" "))
road = input()
# print(road)

i = 0
j = 1
obstacle = False

while i<n-1:

    while j < k and i+j < n:
        if road[i+j] != '#':
            break
        j += 1
        # print(j)
        
    i += j

    if road[i] == '#':
        obstacle = True
        break
    j = 1


if not obstacle:
    print("YES")
else:
    print("NO")