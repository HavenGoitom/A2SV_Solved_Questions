from math import ceil

n = int(input())
coordinates = list(map(int, input().split(" ")))

coordinates.sort()
idx = ceil(n/2)

print(coordinates[idx-1])